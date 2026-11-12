<div align="center">

<img src="assets/icon.png" width="112" alt="auto-newmedia-agents">

# auto-newmedia-agents

### Daily automotive new-media topic monitoring, run by an agent.

**Track new models, competitor moves, policy, owner complaints and viral content in five daily sweeps; drop in a link and get it broken down and filed into a knowledge base.**<br>
These jobs repeat daily and follow fixed steps, which makes them perfect SOPs for an agent.<br>
Create a bot, send it one sentence, and it reads this repo, asks you a few questions, and sets itself up.

[![Stars](https://img.shields.io/github/stars/mingginwan/auto-newmedia-agents?style=flat&color=111111&cacheSeconds=3600)](https://github.com/mingginwan/auto-newmedia-agents/stargazers) [![License](https://img.shields.io/badge/license-MIT-111111)](LICENSE)

**[Quick start](#quick-start)** &nbsp;·&nbsp; **[The bot](#the-bot)** &nbsp;·&nbsp; **[One-line setup](bootstrap.md)** &nbsp;·&nbsp; **[AGENTS.md](AGENTS.md)** &nbsp;·&nbsp; **English** · [简体中文](README.zh-CN.md)

</div>

<br>

This repo is a working SOP and skill pack for Chinese automotive new-media teams. It turns the daily topic meeting into an agent routine: collect signals, grade them A/B/C, push a phone-friendly report, keep a topic ledger, and file reference content into a knowledge base.

**The whole system runs on three rules:**

1. **Scripts do the deterministic work**: collecting, deduping, scoring and logging. Results are reproducible and replayable, never a model's "feeling".
2. **The agent judges**: it reads what the scripts produce, then analyzes, extracts, verifies and reports. If data is missing it says so instead of making things up.
3. **You decide**: the agent only pushes conclusions. Spending money, sending anything out and deleting all need your OK. Every correction you make becomes a new rule in its skills.

## The bot

| Bot | What you do | What it does |
|---|---|---|
| [Automotive topic monitor](bots/auto-topic-monitor/README.md) | Nothing (or your brand and price band) | Three reports a day on what's worth filming in the Chinese auto market: new models, competitor moves, policy, owner complaints, and viral content. Grades A/B/C, keeps a topic ledger, and files reference content into a knowledge base. Uses public web pages and your logged-in browser; no API key required. |

## Which agent

Any agent that can run terminal commands and keep long-lived instructions works: Grok Bot, Muse, Dot, Hermes, OpenClaw, Claude Code, Codex. See [AGENTS.md](AGENTS.md) for the generic steps; each product has its own name for "routines" (scheduled tasks) and "vault" (secret storage).

## Quick start

1. Create a new bot in your agent.
2. Send it the matching sentence from [bootstrap.md](bootstrap.md), for example:

   ```text
   Read AGENTS.md in https://github.com/mingginwan/auto-newmedia-agents and set yourself up as the auto-topic-monitor (automotive topic monitor) bot. Ask me one question at a time.
   ```

3. It asks a few questions, does one run by hand to show you, and only turns it into a routine once you're happy.

The whole process is **do it once → tweak until it's right → save as a skill → schedule as a routine**.

The job descriptions and SOP docs inside the repo are written in Chinese. Agents read them fine, and the bot will talk to you in your language.

## What's inside

```
auto-newmedia-agents/
├── AGENTS.md               setup steps for the agent
├── bootstrap.md            the one sentence to send your bot
├── assets/icon.png
├── bots/auto-topic-monitor/
│   ├── README.md           full SOP
│   ├── job.md              job description
│   ├── routines.md         schedule
│   ├── check.md            acceptance checklist
│   ├── skills/auto-topic-monitor/SKILL.md
│   ├── skills/douyin-comments/   optional: full Douyin comment section
│   └── templates/          report, breakdown and topic-ledger templates
├── lib/runlog/             optional run log
├── templates/              shared ledger formats
└── tests/                  dry-run checks that need no key
```

## Data sources

The automotive topic monitor uses public web pages plus your logged-in browser: automaker sites, Autohome, Dongchedi, 12365auto, MIIT, and Douyin/Xiaohongshu through your own session. **No API key and no paid data service required.** The optional `douyin-comments` skill also runs in your own logged-in browser.

## Optional: run log

For a sturdier setup where you can trace what went wrong, add the [run log module](lib/runlog/README.md). It records whether each routine ran, whether it succeeded, what you approved, and when a rule was changed. It is off by default and only writes local files.

## License

MIT. This project is adapted from [saas-growth-agents](https://github.com/Pluviobyte/saas-growth-agents) by Pluviobyte; see [NOTICE.md](NOTICE.md).
