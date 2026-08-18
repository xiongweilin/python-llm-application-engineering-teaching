# Python, Math, LLM, RAG, and Agent Engineering

This is the only active course. The Windows Start-menu entry is **Python & LLM Application Engineering**; it silently starts the local course server and opens the home page.

## How to continue now

1. Open the course entry in the Start menu.
2. Open formal learning session 2 "Retry, deduplication, and batching".
3. Complete the three distinct problems in order; each problem goes through the seven steps — orientation, underlying logic, Python details, prediction, guided local completion, one bounded change, and summary — and the page shows only one step at a time.
4. Each problem starts with a worked example and an execution trace. The code tasks provide a near-complete scaffold and identify the small part to change; this session does not require designing a solution from a blank page.
5. Once all nine guided tasks across the three problems are done, copy the full evidence on the summary page and interact with the teacher only once.

The learning evidence already formed by problems 1–2 is retained. Prototypes A/B/C have left the active entry; the formal session uses A's single-step skeleton and adds detailed abstract logic and concrete programming explanations.

If the repository location changes, run `pwsh -NoProfile -NonInteractive -File .\runtime\install-start-menu-shortcut.ps1` to idempotently create or update the Start-menu entry. Before replacing the old entry, the script keeps a rollback backup in the local course-state directory.

For review, enter "Comprehensive review of established capabilities" from the home page. It joins the 10 baseline records of ring 0 into one complete session, does not require redoing old problems page by page, and does not change the current formal-session progress. The state-transition records newly formed in formal session 1 are kept separately.

## How the course is organized

Active documents stay minimal but sufficient: each fact type has one owner, history is kept by Git and ADRs, and synonymous overviews or HTML copies are no longer maintained.

- `FINAL-CAPABILITY-CONTRACT.md`: the single source of truth for the course's final capabilities, including the mainline, research extensions, and final synthesis project requirements.
- `index.html`: the only home page and current next step.
- `lessons/`: formal sessions, comprehensive review sessions, completed review pages, and candidate material; pages must declare their identity explicitly, and only formal sessions carry current progress.
- `practice/`: runnable Python exercises with tight feedback.
- `lessons/0010-state-and-permitted-actions.html`: completed formal learning session 1.
- `lessons/0011-integrated-review-established-capabilities.html`: single comprehensive review entry for the 10 established capabilities.
- `lessons/0012-failure-retry-stop.html`: current formal learning session 2.
- Session 3 "Modules, diagnostics, and authorization boundaries" has no formal page yet; when it does, start with spaced recall without answers, then study the three problems of module responsibility, test diagnostics, and authorization boundaries.
- `practice/prototype-guided-session.html`: the selected design prototype, not carrying current progress.
- `reference/0002-course-progress.html`: the single source of truth for the four-stage seventeen-ring structure, ring-level responsibilities, gates, and the final-capability-to-gate coverage index.
- `SESSION-PAGE-CONTRACT.md`: the single specification for formal-session page structure.
- `NOTES.md`: current teaching state, user preferences, and course-generation constraints; does not redefine final capabilities or ring-level routes.
- `RESOURCES.md`: source entries and usage boundaries.
- `docs/decisions/`: records only why the course architecture changed this way; does not replace the capability contract or ring-level routes.
- `reference/`: the full route, cross-session shared terminology, and reference cards with explicit ownership.
- `learning-records/`: capabilities already proven by performance, not learning logs.
- `runtime/`: silent start/stop and auto-verification scripts.

Each formal session and comprehensive review session page has a "本会话中文术语" (Chinese terms of this session) section at the bottom; the shared glossary is only for cross-session review. Page specification lives directly in [SESSION-PAGE-CONTRACT.md](SESSION-PAGE-CONTRACT.md); HTML copies with identical content are no longer maintained.

The course uses a project/theory double spiral with finite representation, finite dimension, and computable models as the mathematical mainline: ring 5 forms beliefs, ring 7 completes single-step choice, ring 8 completes cross-time choice, ring 9 analyzes multi-agent rules, ring 14 connects permissions and human capacity, ring 15 verifies real-world effects. Early Python sessions use worked examples, execution traces, line-by-line comments, local completion, and bounded changes; independent modeling and open-ended design are introduced later as the learner has the required code ownership. See the [course route](reference/0002-course-progress.html) for the full ring design, the [final capability contract](FINAL-CAPABILITY-CONTRACT.md) for graduation requirements, and [architectural decisions](docs/decisions/0001-finite-computable-curriculum-core.md) for why this structure was chosen. Mathematical physics and generalization theory remain research extensions, no longer mainline graduation gates.
