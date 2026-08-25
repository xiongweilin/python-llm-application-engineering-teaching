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

The worked-example step has now produced limited live evidence: the learner reports Python 3.14.7, successfully ran the example file, predicted `True` before execution, and explained the path from `allowed` through the `can_retry` call, parameter values `2` and `4`, the comparison, and the returned `True`. Treat this as execution-and-tracing evidence under full scaffold, not as independent function reconstruction.

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
- A usable local Python runtime and basic `.py` execution are now observed; do not re-teach them unless execution friction reappears.
- Do not yet assume independent Python syntax production from the worked example.
- Introduce each new syntax form before using it as part of a structural assessment.
- Continue the temporary novice sequence: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring new task.
- During imitation, the learner may inspect the worked example.
- Syntax lookup is allowed.
- Do not treat successful transcription or imitation as independent reconstruction evidence.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the execution/syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Obtain one near imitation of the same variable/function/condition/return/call/print structure while the learner may inspect the worked example. Then test one controlled variation without changing multiple syntax dimensions at once. Only after that move to a neighboring new task and eventually return to independent bounded-retry reconstruction.

## Observed friction

The first bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. The learner reported understanding the retry logic while not yet knowing how to run a Python file or what the Python forms in the exercise meant. Treat this as non-target friction, not evidence of structural retry failure.

The first worked example removed the runtime obstruction. No syntax failure has yet been observed during independent production because independent production has not yet been tested.

## Unknowns to resolve from live interaction

- basic Python syntax production and retrieval: literals, variables, function calls, `def`, parameters, return values, indentation, exceptions, classes, and lists;
- whether the learner can reproduce a simple function structure while using the worked example as a reference;
- whether the same structure survives one controlled variation and a neighboring new task;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
