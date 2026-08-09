"""Minimal pytest smoke suite for the course runtime scripts.

The repository keeps its verifiable logic in small zero-dependency scripts
(practice checkers, the local course server, and the content verifier).  This
suite exercises that logic directly so CI can gate changes without depending on
student answers or machine-local paths.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(module_name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_practice_checker_accepts_complete_answers() -> None:
    checker = _load("check_practice_0001", "practice/check_practice_0001.py")

    class CompleteAnswers:
        @staticmethod
        def normalize_name(name: str) -> str:
            return name.strip().lower()

        @staticmethod
        def validate_order(price: int, quantity: int) -> list[str]:
            errors: list[str] = []
            if price <= 0:
                errors.append("价格必须大于0")
            if quantity <= 0:
                errors.append("数量必须大于0")
            return errors

        @staticmethod
        def next_state(current: str, event: str) -> str:
            transitions = {
                ("waiting", "start"): "running",
                ("running", "finish"): "done",
                ("running", "fail"): "failed",
            }
            try:
                return transitions[(current, event)]
            except KeyError as exc:
                raise ValueError(f"invalid transition {current!r} + {event!r}") from exc

        @staticmethod
        def retry(action, max_attempts: int):
            if max_attempts < 1:
                raise ValueError("max_attempts must be positive")
            for _ in range(max_attempts):
                try:
                    return action()
                except RuntimeError:
                    continue
            raise RuntimeError("attempts exhausted")

        @staticmethod
        def create_once(store: dict[str, object], operation_id: str, payload: object):
            if not operation_id:
                raise ValueError("operation_id must not be empty")
            if operation_id in store:
                return store[operation_id], True
            store[operation_id] = payload
            return payload, False

        @staticmethod
        def process_batch(items, handler):
            results: list[object] = []
            errors: list[dict[str, object]] = []
            for position, item in enumerate(items, start=1):
                try:
                    results.append(handler(item))
                except ValueError as exc:
                    errors.append({"position": position, "error": str(exc)})
                except RuntimeError:
                    raise
            return {"results": results, "errors": errors}

    assert checker.run_checks(CompleteAnswers()) == 0


def test_course_server_serves_utf8_text() -> None:
    server = _load("course_server", "runtime/course_server.py")
    handler = server.CourseRequestHandler
    # guess_type only relies on mimetypes and the charset override, so an
    # uninitialized instance is enough to exercise the shared logic.
    instance = object.__new__(handler)
    assert handler.guess_type(instance, "page.html") == "text/html; charset=utf-8"
    assert handler.guess_type(instance, "course.css") == "text/css; charset=utf-8"


def test_verify_content_parser_extracts_links_and_ids() -> None:
    verifier = _load("verify_content", "runtime/verify-content.py")
    parser = verifier.PageParser()
    parser.feed(
        '<html><body><div id="target">'
        '<a href="other.html#frag">link</a>'
        "<script>const x = 1;</script>"
        "</body></html>"
    )
    assert parser.links == ["other.html#frag"]
    assert "target" in parser.ids
    assert len(parser.scripts) == 1 and "const x" in parser.scripts[0]
