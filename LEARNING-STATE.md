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

The novice sequences for simple functions, list/indexing, `for`, explicit `raise`, and basic `try` / `except ValueError:` have each reached one neighboring independent reconstruction for the current prerequisite purpose.

The current new unit is the callback boundary: passing a function itself as a value and calling it through a parameter.

The first worked example has been manually typed and run:

```python
def say_hello():
    print("hello")


def run_action(action):
    action()


run_action(say_hello)
```

The learner correctly predicted and observed `hello`, correctly stated that `say_hello` is not called when it is passed as the argument in `run_action(say_hello)`, identified `action()` as the line that triggers the call, and explained that `action` is a parameter receiving a function. Refine terminology when useful: in this call, the parameter `action` is bound to the `say_hello` function object/value. Treat this as worked-example/manual-typing evidence only, not independent callback reconstruction.

The remaining prerequisite before returning to bounded retry is to stabilize the callback boundary through imitation, one controlled variation, and neighboring reconstruction.

After callback transfer, return to the bounded-retry target:

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

## Curriculum direction after the retry prerequisite closes

Do not expand into a traditional broad Python syllabus. Use real API-facing work units to continue Phase A evidence and then activate a later operational phase only when earned.

Preferred near-term direction after callback and bounded retry:

```text
bounded Python execution baseline
→ small bridge: dict / JSON / import / Path / environment variables / HTTP request-response / status code / timeout / logging
→ real API work units that exercise state, effects, diagnosis, retry, and verification
→ LLM API with structured output and validation
→ tool calling with explicit proposal / validation / authorization / execution / effect verification boundaries
→ MCP tool/server use and modification
→ one bounded, controlled agent project
```

Do not wait for exhaustive Python coverage before introducing real APIs. API work can itself provide Phase A evidence because the current authoritative Phase A gate requires ownership of unfamiliar code, failures, side effects, recovery, authority boundaries, and transfer. Conversely, do not declare a separate Phase B complete merely from one API demo.

The current `CAPABILITY-CONTRACT.md` intentionally has only Phase A as the authoritative gate and keeps later coverage as a future guard. Do not pre-generate a detailed Phase B gate yet. When API/tool/MCP becomes the active domain, define the minimum operational gate then, using live evidence. A likely operational theme is API / Tool / MCP execution ownership.

Mathematics, probability, Transformer internals, RAG theory, games, causality, and evaluation remain required long-term coverage where relevant, but should be pulled forward by actual engineering need rather than inserted as one large prerequisite block before API/tool work.

Shell/PowerShell should remain instrumental rather than a standalone curriculum: enough to navigate, run Python, install/use environments when needed, manage environment variables, start/stop programs, and inspect outputs/errors.

## Current scaffold

- Current default environment: this conversation, VS Code, and a local Python runtime.
- The learner reports Python 3.14.7 and has successfully run multiple `.py` files from the VS Code terminal.
- Basic independent production is observed for literals, assignment, `def`, parameters, `if`, `<`, `return`, calls, returned-value assignment, `print`, list indexing, simple `for`, guarded `raise ValueError(...)`, and basic matching `try` / `except ValueError:`.
- Basic callback semantics have one successful worked example; do not yet assume independent syntax production or transfer.
- Distinguish `function_name` (function object/value) from `function_name()` (call now).
- A parameter can be bound to a function object and later invoked with `parameter()`.
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

Use one near imitation of the callback boundary while the learner may inspect the worked example. Use a neighboring zero-argument function and a runner function that accepts it as a parameter and calls that parameter. Require prediction, runtime output, and explanation of exactly where the passed function is invoked. Then run one controlled variation before a neighboring no-template reconstruction. Do not combine callback imitation with retry yet.

## Observed friction

The original bounded-retry reconstruction mixed retry structure with unknown runtime/editor/Python syntax; treat that as non-target friction.

One earlier execution-order error around uncaught exceptions was corrected with traceback evidence. The explicit-`raise` and `try` / `except` sequences later stabilized raised/skipped/handled paths.

The first callback worked example currently shows no conceptual friction: the learner distinguishes passing a function from calling it and identifies the call-through-parameter line correctly. Verify this under imitation and transfer before treating it as stable.

## Unknowns to resolve from live interaction

- callback syntax production and neighboring transfer;
- whether the learner keeps `function_name` distinct from `function_name()` under variation;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate stopping conditions, side-effect boundaries, and callback invocation boundaries;
- practical ownership of dict/JSON/import/Path/environment/HTTP/logging forms when API work begins;
- whether later API/tool/MCP execution ownership warrants a formal Phase B gate when that domain becomes active;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
