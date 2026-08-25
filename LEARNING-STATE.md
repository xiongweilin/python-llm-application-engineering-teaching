# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 13 retained learning records. They currently support experience with:

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
- independently reconstructing a simple list-plus-indexing structure in a neighboring context.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Build the minimum Python execution and syntax baseline needed to return to bounded-retry reconstruction without mixing syntax friction into the structural assessment.

The initial novice sequence for variables, functions, comparison, return values, calls, assignment, and `print` has completed successfully.

The list/indexing sequence has also completed for the current prerequisite purpose:

```text
worked example
→ manual typing
→ imitation
→ invalid-boundary traceback
→ neighboring reconstruction without a visible template
```

In the neighboring list task, the learner independently created `delays = [1, 2, 4, 8]`, selected the first, third, and fourth elements using indices `[0]`, `[2]`, and `[3]`, predicted and observed `1`, `4`, and `8`, and explained the zero-based mapping correctly. This is retained as scoped independent reconstruction evidence.

The learner also understands that an access such as `delays[4]` is outside the valid index range for a four-element list. Whether any prior values have already been printed depends on the actual location of the failing access relative to the `print` statements; keep execution-order reasoning tied to source order.

The current syntax unit is bounded repetition with `for`. Its first worked example was completed under full scaffold. The learner predicted and observed the output `1`, `2`, `4`, then `done`; identified the loop-variable values as `1`, `2`, and `4`; and correctly explained that `print("done")` runs once because it is outside the indented loop body. Correct terminology when needed: the `for` statement iterates and binds one element at a time; `print(delay)` is what produces terminal output.

The near-imitation step also succeeded. While allowed to inspect the worked example, the learner independently wrote `attempts = [1, 2, 3, 4]`, iterated with `for attempt in attempts:`, printed each attempt, and placed `print("finished")` outside the loop. The learner predicted and observed `1`, `2`, `3`, `4`, then `finished`, identified the four loop-variable values correctly, and explained that `finished` prints once because that statement is unindented and outside the loop body. Treat this as imitation evidence, not yet neighboring independent loop reconstruction.

The controlled indentation variation also succeeded. After moving `print("finished")` into the loop body, the learner correctly predicted and observed the alternating output `1/finished`, `2/finished`, `3/finished`, `4/finished`, stated that `finished` prints four times because the statement is now indented inside the loop, and explained that the changed result comes from the statement's changed relationship to the loop body. This is evidence that indentation is being interpreted as block membership controlling execution count, not merely visual formatting.

Before returning to bounded retry, introduce the remaining syntax needed by retry code one small unit at a time.

Likely remaining prerequisites:

```text
bounded repetition (`for`)
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
- List literals and zero-based indexing are sufficiently stable for the current prerequisite purpose, including one real `IndexError` traceback and one neighboring independent reconstruction.
- `for` has been introduced, traced, reproduced in one near imitation, and tested with one controlled indentation variation; do not yet assume neighboring independent production.
- Do not re-teach already stable forms from scratch unless friction reappears, but keep correcting terminology when useful.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not hidden from the learner.
- When an uncaught exception occurs, distinguish statements executed before the failing line from statements that appear later in the file and therefore never run.
- A function call returns a value; assignment stores that value; `for` iterates/binds values; indentation determines block membership; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Ask for one neighboring loop task without a full template. The learner should independently create a list, iterate over it with `for`, use the loop variable inside the indented body, predict the full output, run it, and explain which statements are inside versus outside the loop. If this succeeds, treat bounded repetition as sufficiently stable for the current prerequisite purpose and introduce exceptions/`raise` with a worked example.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. The simple function sequence and list/indexing sequence have each reached one neighboring independent reconstruction.

One execution-order mistake appeared during the list-boundary experiment: the learner initially expected `print` statements located after an uncaught exception to execute. This was corrected after reading the real traceback. Continue checking source-order reasoning when future exceptions are introduced.

No new friction appeared in the `for` worked example, near imitation, or controlled indentation variation. The learner now correctly reasons that indentation determines loop-body membership and therefore execution count. The remaining uncertainty is neighboring loop reconstruction without a full template.

## Unknowns to resolve from live interaction

- bounded repetition syntax production and transfer in a neighboring task;
- exception, `raise`, and `try` / `except` syntax;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
