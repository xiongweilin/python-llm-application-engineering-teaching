"""Serve the unified course on localhost and support an authorized shutdown."""

from __future__ import annotations

import argparse
import json
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


class CourseRequestHandler(SimpleHTTPRequestHandler):
    shutdown_token = ""

    def guess_type(self, path: str) -> str:
        content_type = super().guess_type(path)
        if content_type.startswith("text/") and "charset=" not in content_type:
            return f"{content_type}; charset=utf-8"
        return content_type

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, _format: str, *args: object) -> None:
        return

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        token = parse_qs(parsed.query).get("token", [""])[0]
        if parsed.path != "/__course__/shutdown" or token != self.shutdown_token:
            self.send_error(403)
            return

        payload = json.dumps({"status": "stopping"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
        threading.Thread(target=self.server.shutdown, daemon=True).start()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--token", required=True)
    parser.add_argument("--state-file", type=Path, required=True)
    parser.add_argument("--url-file", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        raise SystemExit("port must be between 1 and 65535")

    root = Path(__file__).resolve().parent.parent
    CourseRequestHandler.shutdown_token = args.token
    handler = partial(CourseRequestHandler, directory=str(root))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        args.state_file.unlink(missing_ok=True)
        args.url_file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
