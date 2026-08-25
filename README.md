# Python & LLM Application Engineering

This repository is a thin learning control plane for AI-guided study.

It intentionally does **not** pre-generate lessons, web pages, navigation, or a fixed session sequence. Stable constraints and earned evidence live in Git; teaching happens in live dialogue with an AI teacher.

## Continue learning

Ask the AI teacher to read, in order:

1. `TEACHING-CONTRACT.md`
2. `CAPABILITY-CONTRACT.md`
3. `LEARNING-STATE.md`
4. the most relevant recent files in `learning-records/`

Then continue from the current evidence. The teacher should select the next task with the highest information value rather than follow a prewritten lesson page.

The normal loop is:

```text
read current state
→ choose one work unit
→ learner predicts / judges first
→ learner executes against real code or a runnable exercise
→ inspect runtime evidence
→ teach only the observed gap
→ vary or transfer the task
→ update evidence and next state
```

## Repository responsibilities

- `TEACHING-CONTRACT.md` — stable rules for AI intervention, evidence, scaffolding, and curriculum changes.
- `CAPABILITY-CONTRACT.md` — long-term coverage guard and the current Phase A capability gate.
- `LEARNING-STATE.md` — small, current, revisable state used to resume teaching.
- `learning-records/` — capabilities already supported by performance evidence; not a diary and not a list of pages viewed.
- `practice/` — runnable exercises created only when a live learning need requires them.

Git history is the history mechanism. Do not create duplicate progress dashboards or prose copies of the same fact.

## Current focus

Phase A: Python and real-system code ownership. The immediate target is to turn existing structural understanding into reliable reconstruction, modification, diagnosis, and transfer in runnable Python work units.

## Evidence discipline

Seeing an answer is not mastery. Imitation is not independent reconstruction. A passing checker is not transfer. Syntax lookup is not evidence of structural failure. AI judgment is provisional; learner performance and runtime evidence decide whether capability state changes.

## License

MIT.
