# GitStar AI ⭐

<p align="center">
  <b>Open-source AI engineering operating system for agent loops, memory-backed workflows, reusable skills, and GitHub automation.</b>
</p>

<p align="center">
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="./LOOP.md"><img alt="Loop Ready" src="https://img.shields.io/badge/loop--ready-L1-green.svg"></a>
  <a href="./STATE.example.md"><img alt="Memory" src="https://img.shields.io/badge/memory-STATE.md-purple.svg"></a>
  <a href="./patterns"><img alt="Patterns" src="https://img.shields.io/badge/patterns-4-orange.svg"></a>
</p>

<p align="center">
  <b>Stop prompting from scratch. Start designing repeatable AI workflows.</b>
</p>

GitStar AI helps developers turn scattered prompts, GitHub projects, agent instructions, and business workflows into reusable **AI operating loops**.

> Design the loop. Let agents execute. Keep humans in control.

---

## Why GitStar AI?

Most AI workflows fail because they live inside one chat window.

GitStar AI gives your agents a simple operating system:

```text
Goal
  ↓
Loop
  ↓
Skill
  ↓
Memory / State
  ↓
Agent Execution
  ↓
Verification
  ↓
Human Approval
  ↓
Action
```

Use it with Codex, Claude Code, Cursor, Grok, GitHub Actions, n8n, Supabase, Cloudflare, Telegram, or your own local tools.

---

## What You Can Build

| Workflow | Example |
|---|---|
| 🧠 Daily Triage | Summarize repo/project status and next actions |
| 💹 Trading Watch | Create educational market-watch cards with invalidation levels |
| 🏢 ERP CEO Brief | Draft AP/AR, PO risk, vendor follow-up, and shipment summaries |
| 🎬 Content Factory | Generate scripts, visual prompts, captions, thumbnails, and publish drafts |
| 🛠 GitHub Maintenance | Review issues, PRs, CI failures, dependencies, and changelogs |

---

## Repository Structure

```text
gitstar-ai/
├── README.md
├── LOOP.md
├── STATE.example.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── docs/
│   ├── architecture.md
│   └── policy.md
├── patterns/
│   ├── daily-triage/
│   ├── trading-watch/
│   ├── content-factory/
│   └── erp-ceo-brief/
├── skills/
│   ├── trading.md
│   ├── content.md
│   └── erp.md
├── scripts/
│   └── run_loop.py
└── .github/workflows/
    └── validate.yml
```

---

## Quick Start

```bash
git clone https://github.com/Ramvibecode/gitstar-ai.git
cd gitstar-ai
cp STATE.example.md STATE.md
cp .env.example .env
```

Run a loop manually:

```bash
python scripts/run_loop.py patterns/daily-triage/loop.md
```

Then paste the loop output plus `STATE.md` into your AI coding agent.

---

## Starter Loop Patterns

### 1. Daily Triage
Use this when you want a daily summary of what changed, what is blocked, and what should happen next.

```bash
python scripts/run_loop.py patterns/daily-triage/loop.md
```

### 2. Trading Watch
Creates educational market-watch summaries and risk-defined setup cards.

Best for: BTC, ETH, stocks, options watchlists.

### 3. ERP CEO Brief
Creates leadership summaries for AP, AR, PO lifecycle, shipment risk, documents, and vendor follow-up.

Best for: operations, supply chain, finance, ERP dashboards.

### 4. Content Factory
Turns content ideas into scripts, visual prompts, captions, thumbnails, and approval-ready drafts.

Best for: YouTube Shorts, Instagram Reels, faceless content, original AI characters.

---

## Core Principles

### 1. Human-in-the-loop first
GitStar AI starts in report-only mode. Risky actions need approval.

### 2. Memory outside the chat
`STATE.md` becomes the project memory so every agent starts with context.

### 3. Skills over random prompts
Reusable instructions live in `skills/`, making outputs more consistent.

### 4. Verification before action
Every loop should define what must be checked before publishing, sending, merging, or posting.

---

## Safety Defaults

- No auto-merge by default.
- No secrets committed to Git.
- No financial advice or guaranteed profit language.
- No auto-publishing without review.
- No email sending without approval.
- No copied third-party code without license review.

---

## Roadmap

See [`ROADMAP.md`](./ROADMAP.md).

Planned next:

- More loop patterns
- n8n workflow examples
- Telegram draft workflow
- GitHub issue triage template
- Web dashboard prototype
- Loop readiness scoring

---

## Who Is This For?

GitStar AI is for builders who use AI agents for real work:

- solo developers
- indie hackers
- AI automation builders
- operations teams
- content automation creators
- traders building educational market-watch tools
- teams using Codex, Claude Code, Cursor, Grok, or GitHub Actions

---

## Star This Repo If...

- you are tired of repeating the same AI prompts
- you want reusable agent workflows
- you want project memory that survives chat windows
- you are building AI automation safely
- you believe the future is not prompts, but loops

---

## Contributing

Contributions are welcome. Start with [`CONTRIBUTING.md`](./CONTRIBUTING.md).

Good first contributions:

- add a new loop pattern
- improve an existing skill
- add a verification checklist
- create a simple workflow example
- improve documentation

---

## License

MIT — see [`LICENSE`](./LICENSE).
