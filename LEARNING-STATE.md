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

The worked-example step produced limited live evidence: the learner reports Python 3.14.7, successfully ran the example file, predicted `True` before execution, and explained the path from the function call through parameter values, comparison, returned value, assignment, and `print`. Treat this as execution-and-tracing evidence under full scaffold, not as independent function reconstruction.

The imitation step also succeeded. While allowed to inspect the worked example, the learner independently typed a structurally equivalent `has_room` function, predicted `True`, observed `True`, and explained why the comparison `3 < 5` caused the function to return `True` and the result to be printed. The learner reused the outer names `attempt` and `max_attempts` instead of the suggested `items` and `capacity`; the program still behaved correctly. This is useful evidence that the learner is beginning to separate identifier names from the values passed into parameters. It remains imitation evidence, not independent reconstruction evidence.

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
- Basic tracing of variables, a two-parameter function call, `if`, `return`, assignment, and `print` has been observed under full scaffold and one near imitation.
- Do not yet assume independent Python syntax production from a behavior contract.
- Introduce each new syntax form before using it as part of a structural assessment.
- Continue the temporary novice sequence: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring new task.
- Syntax lookup is allowed.
- Do not treat successful transcription or imitation as independent reconstruction evidence.
- Correct terminology when needed: a function call returns a value; assignment stores that value; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the execution/syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Test one controlled variation of the same function structure without introducing unrelated syntax. Prefer a boundary-value change first so the learner must reason about the existing `<` condition rather than merely repeat the previous successful path. If that succeeds, move to a neighboring new task with the same already-introduced syntax before adding new forms.

## Observed friction

The first bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. The learner reported understanding the retry logic while not yet knowing how to run a Python file or what the Python forms in the exercise meant. Treat this as non-target friction, not evidence of structural retry failure.

The first worked example removed the runtime obstruction. The imitation did not expose a syntax-production failure, but it was still performed with the reference structure available. One terminology issue remains useful to correct: the learner described the result variable as if it called the function; the actual order is function call → returned value → assignment → `print`.

## Unknowns to resolve from live interaction

- basic Python syntax production and retrieval without a visible template: literals, variables, function calls, `def`, parameters, return values, indentation, exceptions, classes, and lists;
- whether the same simple function structure survives one controlled boundary variation and a neighboring new task;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
