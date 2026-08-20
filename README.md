# Python, Math, LLM, RAG, and Agent Engineering

[![CI](https://github.com/ratiolin/python-llm-application-engineering-teaching/actions/workflows/ci.yml/badge.svg)](https://github.com/ratiolin/python-llm-application-engineering-teaching/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
This is the only active course. The Windows Start-menu entry is **Python & LLM Application Engineering**; it silently starts the local course server and opens the home page.

## How to continue now

1. Open the course entry in the Start menu.
2. Open formal learning session 2 "Controlled retry: one complete work unit".
3. Work through the single complete retry work unit: foundation and worked trace, full imitation, full reconstruction, one controlled variation, then transfer to a new fetch scenario.
4. The three task stages are evidence stages — pattern acquisition, controlled variation, and transfer/chunking — rather than three unrelated problems. Full imitation is practice, not independent mastery evidence.
5. Each stage shows line-by-line comments, semantic types, a prediction-before-runtime check, explicit editable loci, syntax cards, and a gradually fading reconstruction scaffold. The session does not require designing a solution from a blank page without a behavior contract.
6. Copy the complete work-unit evidence on the summary page, including R/T/P/M/D/X evidence, help levels used, runtime results, and what remains uncertain; interact with the teacher only once.

Previously formed learning evidence is retained. Prototypes A/B/C have left the active entry; the formal session uses a single-step focus skeleton and adds detailed abstract logic and concrete programming explanations.

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
- `lessons/0012-failure-retry-stop.html`: current formal learning session 2, one complete retry work unit.
- Session 3 "Modules, diagnostics, and authorization boundaries" has no formal page yet; when it does, start with spaced recall without answers, then study one complete diagnostic work unit at a time.
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

## Scope and teaching-mode calibration

The course aims at **minimum operational models**: finite, computable, and usable for advanced AI-systems judgment. It is not a compressed mathematics, computer-science, mechanism-design, or causal-inference degree. Each domain has its own Minimum Viable Judgment threshold — Python/engineering, probability, optimization, sequential decision, RAG/Agent, and causal/reliability — so reaching a threshold in one domain does not remove scaffolding in another.

Open questions are versioned rather than forgotten. A real question receives `J0`, then returns after relevant learning as `J1`, `J2`, and so on; each revision records the new evidence and what changed. The final project also requires applicability judgment: use a theory tool when the reality, assumptions, and evidence justify it; if a tool is not applicable, explain why and use a neighboring real subproblem rather than forcing an artificial MDP, mechanism, or causal model.

The AI intervention contract is: **as learner capability rises, answer supply falls and problem-space supply rises**. Early AI explains and demonstrates, middle-stage AI coaches and stress-tests, and later AI acts as a high-level discussion partner and candidate-map generator. The learner retains framing and judgment authority.

The course uses a project/theory double spiral with finite representation, finite dimension, and computable models as the mathematical mainline: ring 5 forms beliefs, ring 7 completes single-step choice, ring 8 completes cross-time choice, ring 9 analyzes multi-agent rules, ring 14 connects permissions and human capacity, ring 15 verifies real-world effects. The teaching process runs two coupled loops: **worked example → reconstruction → controlled change → transfer → stable-structure explanation**, and **real question → current judgment → expert view → identified gap → targeted foundation → revised judgment**. Early Python sessions treat the learner as a reactivation learner and explicitly translate **reality → program responsibility → code location → Python form → learner action → runtime evidence**. Syntax friction is lowered with visible first-use explanations, line-by-line comments, explicit editable loci, and fading help; each quantity receives a semantic type, each task has one main unknown, and answer-echo items are rejected. Control-flow prediction, failure diagnosis, boundary judgments, local ownership, and bounded changes remain real evidence. Every 2–3 formal sessions also includes a short, non-gated open-question window so the learner can name a current judgment, an uncertainty, and a useful foundation gap. A Minimum Viable Judgment threshold determines when a work domain switches from scaffold-first teaching to **behavior contract → learner judgment → implementation/diagnosis**, with scaffolding restored when evidence shows a need. See the [course route](reference/0002-course-progress.html) for the full ring design, the [final capability contract](FINAL-CAPABILITY-CONTRACT.md) for graduation requirements, and [architectural decisions](docs/decisions/0001-finite-computable-curriculum-core.md), [the reactivation decision](docs/decisions/0003-reactivation-learner-and-fading-support.md), [the translation-layer decision](docs/decisions/0005-phase-a-translation-layer-and-diagnostic-help.md), [the semantic-evidence decision](docs/decisions/0006-phase-a-semantic-types-and-non-echo-evidence.md), and [the open-judgment decision](docs/decisions/0008-open-judgment-and-threshold-switch.md) for why this structure was chosen. Mathematical physics and generalization theory remain research extensions, no longer mainline graduation gates.

