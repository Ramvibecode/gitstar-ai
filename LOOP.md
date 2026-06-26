# LOOP.md

This file defines how GitStar AI loops should operate.

## Default Loop Lifecycle

1. Read `STATE.md`
2. Identify the active goal
3. Gather context
4. Propose next action
5. Execute only safe or allowed actions
6. Run verification checks
7. Update `STATE.md`
8. Ask for human approval if risk is high

## Maturity Levels

| Level | Mode | Description |
|---|---|---|
| L1 | Report-only | Summarize and recommend. No writes. |
| L2 | Assisted | Draft changes and wait for approval. |
| L3 | Limited automation | Safe allowlisted actions only. |

## Hard Rules

- Never expose secrets.
- Never make financial guarantees.
- Never publish external content without approval.
- Never copy third-party code without license review.
- Always leave a run log.
