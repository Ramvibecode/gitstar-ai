# GitStar AI ⭐

**Open-source AI engineering operating system for building agent loops, reusable skills, memory-backed workflows, and GitHub-powered automation.**

GitStar AI helps developers move from one-off prompting to repeatable AI workflows.

> Design the loop. Let agents execute. Keep humans in control.

## What is GitStar AI?

GitStar AI is a practical starter framework for organizing AI coding agents, workflow loops, memory files, GitHub Actions, and domain-specific skills into one repeatable system.

It is not another chatbot. It is a repo structure and operating playbook for making tools like Codex, Claude Code, Cursor, Grok, n8n, Supabase, Cloudflare, and GitHub Actions work together safely.

## Core Ideas

- **Loops** — recurring workflows that triage, plan, execute, verify, and hand off.
- **Memory** — durable project state outside the chat window.
- **Skills** — reusable domain instructions for specific work.
- **Checks** — verification before publishing or merging.
- **Human Gates** — approval points before risky actions.

## Example Use Cases

| Module | What it does |
|---|---|
| Trading Watch | Tracks BTC/ETH/stocks setup ideas and creates educational market-watch cards |
| ERP CEO Brief | Generates AP/AR, PO risk, vendor follow-up, and CEO summary workflows |
| Content Factory | Turns ideas into scripts, visuals, captions, thumbnails, and publish drafts |
| GitHub Triage | Summarizes issues, PRs, CI failures, and next actions |

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/gitstar-ai.git
cd gitstar-ai
cp STATE.example.md STATE.md
cp .env.example .env
```

Run a loop manually:

```bash
python scripts/run_loop.py patterns/daily-triage/loop.md
```

## Repository Structure

```text
gitstar-ai/
├── README.md
├── STATE.example.md
├── LOOP.md
├── docs/
├── patterns/
├── skills/
├── scripts/
└── .github/workflows/
```

## Safety Principles

- Report-only first.
- No auto-merge by default.
- No financial advice.
- No publishing without approval.
- Respect licenses of referenced projects.
- Keep secrets out of Git.

## License

MIT
