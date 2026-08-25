# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 12 retained learning records. They currently support experience with:

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
- implementing and transferring constrained state transitions;
- independently reconstructing one simple Python function structure in a neighboring context.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Build the minimum Python execution and syntax baseline needed to return to bounded-retry reconstruction without mixing syntax friction into the structural assessment.

The initial novice sequence for variables, functions, comparison, return values, calls, assignment, and `print` has completed successfully:

```text
worked example
→ manual typing
→ imitation
→ controlled boundary variation
→ neighboring reconstruction without a visible template
```

The neighboring task (`needs_heating`) was reconstructed correctly from natural-language requirements. The learner predicted `True`, observed `True`, and explained the execution path as variables → function definition → function call → comparison → returned value → assignment → printed output. This is retained as scoped independent reconstruction evidence.

The current syntax unit is Python list values and zero-based indexing. Its worked example was completed under full scaffold, and the list imitation step also succeeded with `[3, 6, 9]` and indices `[0]`, `[1]`, and `[2]`.

The controlled list-boundary variation has now been run. The learner correctly predicted that accessing index `[3]` in a three-element list would fail and supplied the real traceback showing `IndexError: list index out of range` at `third_time = response_times[3]`. The learner incorrectly predicted that the later `print(first_time)` and `print(second_time)` statements would execute before the error. Treat this as useful control-flow evidence: the remaining gap is execution-order tracing across an uncaught runtime exception, not list-index understanding.

Before returning to bounded retry, introduce the remaining syntax needed by retry code one small unit at a time, using the same sequence when a form is genuinely new. Likely prerequisites include:

```text
list values / indexing
→ repetition (`for` or another bounded loop form)
→ exceptions and `raise`
→ `try` / `except`
→ passing a function as a value / callback boundary
```

Do not introduce all of these in one exercise.

The later retry target remains:

```text
trace
→ reconstruct from behavior contract
→ modify one retry rule
→ diagnose an unseen retry failure
→ transfer without being told the pattern name
```

The key retry distinction remains:

```text
whether another attempt is permitted
!=
how long to wait if another attempt is permitted
```

A successful provider call, a candidate delay value, and an actually executed wait are separate events.

## Current scaffold

- Current default environment: this conversation, VS Code, and a local Python runtime.
- The learner reports Python 3.14.7 and has successfully run multiple `.py` files from the VS Code terminal.
- Basic independent production is observed for literals, variable assignment, `def`, two parameters, `if`, `<`, `return`, function call, assignment of the returned value, and `print`.
- List literal and zero-based indexing have been introduced, traced, reproduced in one near imitation, and tested at the invalid upper boundary.
- Do not re-teach already stable forms from scratch unless friction reappears, but keep correcting terminology when useful.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not as something to hide from the learner. When introducing an error type, first let the learner predict the failure, then run it, then read the traceback from the bottom upward: exception type/message, failing line, then local cause.
- When an uncaught exception occurs, explicitly distinguish statements executed before the failing line from statements that appear later in the file and therefore never run.
- A function call returns a value; assignment stores that value; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

First have the learner read the current traceback and identify: (1) exception type, (2) human-readable message, (3) failing source line, and (4) why the later print statements did not execute. Then ask for one neighboring list task without a full template before moving to bounded repetition.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. No significant syntax failure appeared in the simple function sequence. One terminology issue was corrected during the sequence: the result variable does not call the function; the function call happens first, its returned value is assigned, and `print` later produces terminal output.

List indexing itself appears understood, including zero-based indices and the invalid `[3]` boundary for a three-element list. A new trace-order friction appeared: the learner expected print statements located after the failing line to execute before the uncaught exception. Resolve this with the current traceback before adding new syntax.

## Unknowns to resolve from live interaction

- whether the learner can read a simple traceback from bottom to source line;
- whether execution-order tracing now survives an uncaught runtime exception;
- list literal and indexing production in a neighboring task without a complete template;
- bounded repetition syntax and traceability;
- exception, `raise`, and `try` / `except` syntax;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
