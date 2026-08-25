# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 11 retained learning records. They currently support experience with:

- functions and deterministic gates;
- data scope and rule placement;
- status-driven actions;
- lock scope versus status scope;
- recovery responsibility around short transactions;
- bounded retry and time separation;
- operation identity and database uniqueness;
- locating modules by responsibility;
- method chaining and mutation;
- accumulating errors versus fail-fast control flow;
- implementing and transferring constrained state transitions.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Turn the existing conceptual understanding of bounded retry into reliable code-level capability:

```text
trace
→ reconstruct from behavior contract
→ modify one retry rule
→ diagnose an unseen retry failure
→ transfer without being told the pattern name
```

The target distinction is:

```text
whether another attempt is permitted
!=
how long to wait if another attempt is permitted
```

A successful provider call, a candidate delay value, and an actually executed wait are separate events.

## Current scaffold

- Syntax lookup is allowed.
- Do not begin with a full reference implementation unless evidence shows it is needed.
- Prefer a small behavior contract plus tests or runtime observations.
- The learner predicts before execution.
- Help should identify the actual obstruction layer rather than reveal the entire solution.

## Next evidence target

First test independent reconstruction of one bounded-retry work unit from a compact behavior contract. If reconstruction is structurally sound, move immediately to one controlled variation and then an unfamiliar near-transfer case. If it fails, restore only the missing scaffold layer.

## Unknowns to resolve from live interaction

- current Python syntax retrieval friction;
- whether retry structure can be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
