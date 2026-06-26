# Daily Triage Demo

This demo shows how a GitStar AI loop turns project state into a useful report.

## Input

```text
Project: GitStar AI
Current goal: Make the repo useful for AI builders
Recent changes: README polished, loop patterns added
Open risks: no demo yet, no screenshots yet
```

## Loop

```bash
python scripts/run_loop.py patterns/daily-triage/loop.md
```

## Expected Output

```text
GitStar AI Daily Triage

Status: Early public starter

What changed:
- README improved
- Loop patterns added
- Safety policy added

Needs attention:
1. Add first demo
2. Add visual diagram
3. Add issue templates

Recommended next action:
Create a small demo showing how STATE.md and a loop pattern produce an AI-ready task brief.
```
