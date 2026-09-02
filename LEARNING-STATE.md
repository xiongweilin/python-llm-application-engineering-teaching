# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 16 retained learning records. They currently support experience with:

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
- independently reconstructing one simple Python function structure in a neighboring context;
- independently reconstructing a simple list-plus-indexing structure in a neighboring context;
- independently reconstructing a simple `for` loop in a neighboring context;
- independently reconstructing a simple `if` + `raise ValueError(...)` validation structure in a neighboring context;
- independently reconstructing a simple `try` / `except ValueError:` structure in a neighboring context.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Build the minimum Python execution and syntax baseline needed to return to bounded-retry reconstruction without mixing syntax friction into the structural assessment.

The novice sequences for simple functions, list/indexing, `for`, explicit `raise`, and basic `try` / `except ValueError:` have each now reached one neighboring independent reconstruction for the current prerequisite purpose.

The `try` / `except` sequence included a target-specific distinction gap. The learner initially compressed “no traceback” into “no exception happened.” The §2 conditional `Distinction judgment` specialization was applied only because this difference changes control-flow prediction and explanation. The learner learned to retain three materially different states:

- exception never raised;
- exception raised and handled;
- exception raised and unhandled.

A later controlled comparison and the final neighboring reconstruction both preserved this distinction. In the neighboring task, the learner independently wrote a `try` block containing `raise ValueError("invalid price")`, a matching `except ValueError:` printing `price handled`, and a later unindented `print("finished")`; predicted and observed the exact output; stated that the `ValueError` really occurred at `raise`; explained why the matching handler runs and why no traceback appears; and explained that `finished` is both outside the structure and runtime-reachable because the exception was handled. This is retained as scoped independent reconstruction evidence.

The next new syntax/semantics prerequisite is passing a function itself as a value and calling it through a parameter: the callback boundary.

Remaining prerequisite before returning to bounded retry:

```text
function as value / callback boundary
```

Do not mix the callback introduction with retry logic yet.

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
- Basic independent production is observed for literals, assignment, `def`, parameters, `if`, `<`, `return`, calls, returned-value assignment, `print`, list indexing, simple `for`, guarded `raise ValueError(...)`, and basic matching `try` / `except ValueError:`.
- Matching `except` handles an exception that really occurred; no traceback does not imply no exception.
- Block membership / indentation is not the same as runtime reachability.
- Introduce genuinely new syntax before structural assessment.
- For a new syntax form, prefer: explicit worked example → manual typing → imitation → one controlled variation → neighboring use, inserting a targeted judgment check only when evidence shows a consequential classification gap.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors are observable evidence to inspect.
- Add another tool only when it has a concrete learning or engineering purpose and explain that purpose first.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Introduce the callback boundary with one tiny worked example and no retry logic. Use one ordinary zero-argument function that prints a known message, and a second function that accepts a parameter representing a function and calls that parameter with parentheses. The learner should manually type the full example, predict the output, run it, and explain the distinction between passing `say_hello` and calling `say_hello()`. Do not introduce lambdas, higher-order terminology, decorators, or retry in the first callback example.

## Observed friction

The original bounded-retry reconstruction mixed retry structure with unknown runtime/editor/Python syntax; treat that as non-target friction.

One earlier execution-order error around uncaught exceptions was corrected with traceback evidence. The explicit-`raise` sequence later stabilized raised versus skipped paths.

The first `try` / `except` example exposed the compression “no traceback means no exception.” A targeted distinction-judgment check corrected it, the distinction briefly reappeared during imitation, and a controlled never-raised versus raised-and-handled comparison stabilized it. The final neighboring `try` / `except` reconstruction preserved the correct distinction. Treat this issue as resolved unless it reappears under later transfer.

## Unknowns to resolve from live interaction

- passing a function object/value as an argument;
- distinguishing `function_name` from `function_name()`;
- calling a received function parameter inside another function;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
