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

Before resuming bounded-retry reconstruction, establish the minimum Python execution and syntax baseline needed for code-level work:

```text
create a .py file in VS Code
→ understand how to run it with the local Python runtime
→ manually type and run one complete worked example
→ explain the role of each syntax form used
→ reproduce the same structure with light guidance
→ make one controlled variation
→ solve a neighboring new task
```

Once these actions stop being the obstruction, return to the existing bounded-retry target:

```text
trace
→ reconstruct from behavior contract
→ modify one retry rule
→ diagnose an unseen retry failure
→ transfer without being told the pattern name
```

The retry target distinction remains:

```text
whether another attempt is permitted
!=
how long to wait if another attempt is permitted
```

A successful provider call, a candidate delay value, and an actually executed wait are separate events.

## Current scaffold

- Current default environment: this conversation, VS Code, and a local Python runtime.
- Do not assume the learner already knows how to run a `.py` file, use the VS Code terminal, or interpret Python syntax used in the task.
- Introduce each new syntax form before using it as part of a structural assessment.
- Use the temporary novice sequence: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring new task.
- Syntax lookup is allowed.
- Do not treat successful transcription or imitation as independent reconstruction evidence.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the execution/syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

First establish that the learner can create and run a small Python file in VS Code and can explain the basic syntax used in that file. Then obtain one imitation and one controlled-variation success without hiding syntax friction. Only after that return to independent reconstruction of the bounded-retry work unit.

## Observed friction

The first bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. The learner reported understanding the retry logic while not yet knowing how to run a Python file or what the Python forms in the exercise meant. Treat this as non-target friction, not evidence of structural retry failure.

## Unknowns to resolve from live interaction

- whether a usable local Python runtime is already installed and which command invokes it;
- VS Code terminal and file execution familiarity;
- basic Python syntax retrieval: literals, variables, function calls, `def`, parameters, return values, indentation, exceptions, classes, and lists;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
