# Architecture

GitStar AI uses a simple control system:

```text
Goal → Loop → Skill → Context → Agent → Verification → Human Gate → State Update
```

## Components

### Loops
Repeatable workflows that run manually, on schedule, or through automation.

### Skills
Reusable instruction files for domains like trading, ERP, content, GitHub triage, and security.

### Memory / State
A durable `STATE.md` file records project status, decisions, and next actions.

### Verification
Every loop should define checks before output is trusted.

### Human Gate
Important actions require approval before publishing, sending, merging, or acting.
