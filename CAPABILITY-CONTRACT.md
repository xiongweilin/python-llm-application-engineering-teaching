# Capability Contract

This file prevents live, adaptive teaching from optimizing only for the current task and silently dropping important long-term capabilities.

It intentionally defines **what must eventually be possible**, not a fixed lesson sequence.

## Long-term outcome

Independently design, implement, evaluate, and maintain reliable, controlled, recoverable LLM workflows or RAG/agent systems; form minimum operational models for uncertainty, decision, sequential behavior, multi-agent interaction, and system evaluation; and connect those models to real state, permissions, capacity, verification, recovery, and rollback boundaries.

Mainline models should remain finite, finite-dimensional, computable, enumerable, solvable, simulatable, or numerically checkable unless a real problem earns the need for a stronger abstraction.

Do not conflate:

```text
finite model != general theory
simulation != proof
model score != probability of correctness
content correctness != authority to act
provider success != real-world objective completion
```

## Current authoritative gate: Phase A

Phase A is complete only when the learner has practical ownership of bounded Python and real-system code, rather than familiarity with syntax or lesson examples.

The learner should be able to:

1. **Read and map unfamiliar code** — identify objects, state, rules, interfaces, control flow, data flow, side effects, and the module or function that owns a responsibility.
2. **Trace execution** — predict and explain representative normal, failure, and boundary paths before checking runtime evidence.
3. **Reconstruct from a behavior contract** — implement the main structure without needing a full reference solution; syntax lookup is allowed.
4. **Modify with boundaries** — change one or more intended rules while preserving stated invariants and verifying the result.
5. **Diagnose unseen failures** — use tests, traceback, logs, state, and local code inspection to locate the responsible layer instead of guessing from symptoms.
6. **Reason about state and effects** — distinguish operation state, environment state, retries, idempotency, recovery, and external side effects where they matter.
7. **Respect authority boundaries** — distinguish model output or candidate code from an authorized external action; identify when an operation may propose, verify, approve, execute, or compensate.
8. **Transfer** — recognize and use a stable structure in a neighboring unfamiliar task and, eventually, in real project code without being told the pattern name in advance.

### Phase A teaching-mode threshold

A work domain has reached Minimum Viable Judgment only when the above abilities survive both:

- an answer-free interval; and
- an unfamiliar neighboring task or real code fragment.

MVJ is not Phase A completion. It only means the teacher should stop leading with worked examples in that domain.

## Future coverage guard

Later learning must eventually cover enough operational judgment in the following domains. Detailed gates should be specified only when those domains become active; do not pre-generate their lessons now.

- mathematical language, probability, statistics, calibration, and evidence boundaries;
- linear algebra, tensors, and numerical shape reasoning;
- calculus, constrained optimization, resource allocation, and single-step decision under uncertainty;
- state evolution, Markov models, sequential decision, exploration, and value of information;
- language-model probability, Transformer computation, training basics, and numerical failure modes;
- embeddings, retrieval, evaluation, RAG, agent workflows, tool use, memory, and human escalation;
- finite games, incentives, aggregation, allocation, and mechanism analysis;
- experiment design, causal evaluation, reliability, recovery, and effect verification.

A later domain must justify its own assumptions and evidence. Competence in one domain does not automatically close another.

## Graduation evidence

Course completion ultimately requires cross-domain transfer and a synthesis project in which the learner can:

- frame a real problem;
- choose an applicable representation rather than force a favorite model;
- implement and test the system;
- distinguish epistemic evidence, decisions, authorization, execution, and real-world effects;
- diagnose failure and revise the representation when evidence invalidates it;
- explain the scope and remaining uncertainty of the result.
