# Robotics Roadmap — 6 Month Tracker

![Progress](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Ojotule-Benjamin/robotics-roadmap/main/.github/badges/progress.json)

A day-by-day checklist for the 6-month "electronics → embedded → mechanical →
ROS 2 → controls/perception → robot learning" roadmap. Built to live in a
git repo so progress is tracked in commit history, not just in your head.

## How this works

- Each month has its own file: `month-1-electronics.md` … `month-6-robot-learning.md`.
- Each day is a GitHub-flavored checkbox: `- [ ] Day N — task`.
- When you finish a day's task, edit the box to `- [x]`, then commit:

```bash
git add month-1-electronics.md
git commit -m "Day 7: built voltage divider, verified in Falstad"
git push
```

- One commit per study day, referencing the day number, keeps a visible
  streak in your contribution graph and a running log of what you actually did.
- `PROGRESS.md` is the top-level dashboard — tick off month milestones there
  once every day-box in that month's file is checked.
- `logs/` is for the single highest-value habit in the whole roadmap: writing
  down what broke. Use `logs/TEMPLATE.md` — copy it to `logs/day-007.md` (etc.)
  whenever something fails and you fix it. These become the backbone of your
  portfolio READMEs later.

## Pace

Roughly 2–3 hours/day, ~5 study days a week. Day counts per month are weighted
by how much content that month covers (Month 2 and Month 4 are the heaviest).
Skip a day, no problem — the checklist doesn't expire, just keep committing
when you actually did the work. Don't tick a box you haven't done; the point
of tracking this on git is that the history has to be honest to be useful.

## Checking your progress

Run the tracker script any time to see a per-month breakdown and your commit streak:

```bash
python scripts/progress.py
```

The badge at the top of this README updates itself automatically: a GitHub
Actions workflow (`.github/workflows/progress-badge.yml`) runs the same
script whenever you push changes to a `month-*.md` file and commits the
result to `.github/badges/progress.json`. Nothing to set up — it just works
once this is pushed to GitHub, using the `contents: write` permission
Actions gets by default.

## Documenting what you learn

`notes/` is separate from `logs/`: `logs/` is for debugging failures
("what broke"), `notes/` is for concepts you're learning as you read/watch
each resource. Copy `notes/TEMPLATE.md` to a new file per topic (e.g.
`notes/month-1-static-electricity.md`) and fill it in **in your own words**
right after finishing a resource — not while reading it. The template
forces a few things that actually help retention: explaining without
re-reading the source, linking the idea to something you already know, and
a delayed recall check you fill in a few days later without peeking at your
first attempt. See `notes/month-1-static-electricity.md` for a filled-out
example.

## Logging what broke


Two ways to use `logs/TEMPLATE.md`:
- Copy it locally to `logs/day-XXX.md` and commit it alongside that day's work, or
- Open a GitHub Issue using the **"What broke (debug log)"** template
  (`.github/ISSUE_TEMPLATE/what-broke.md`) — same questions, but lets you
  search/filter your debugging history from the Issues tab instead of the
  file tree.

Either is fine — pick whichever you'll actually keep up.

## Suggested repo layout

```
robotics-roadmap/
├── README.md
├── PROGRESS.md
├── RESOURCES.md            ← every course/doc/tool link, by month
├── SHOPPING-LIST.md        ← every part to buy, prices, vendors, budget tiers
├── month-1-electronics.md
├── month-2-microcontrollers.md
├── month-3-cad-manufacturing.md
├── month-4-ros2-simulation.md
├── month-5-controls-perception.md
├── month-6-robot-learning.md
├── scripts/
│   └── progress.py         ← prints % complete + commit streak, feeds the badge
├── notes/
│   ├── TEMPLATE.md         ← for concepts you're learning (own words + recall check)
│   └── month-1-*.md        (one per topic)
├── logs/
│   ├── TEMPLATE.md         ← for debugging failures ("what broke")
│   └── day-XXX.md   (one per failure worth documenting)
├── projects/
│   └── (each build gets its own folder: code, wiring notes, photos/video links)
└── .github/
    ├── workflows/progress-badge.yml   ← auto-updates the README badge
    ├── badges/progress.json           ← generated, don't hand-edit
    └── ISSUE_TEMPLATE/what-broke.md   ← "what broke" log as a GitHub Issue
```

Every day's checklist item now has its resource link **inline** — you
shouldn't need to leave the month file you're working from. `RESOURCES.md`
and `SHOPPING-LIST.md` still exist as full standalone references (every
link/price in one place, useful for browsing ahead or re-finding something),
but day-to-day you can just work straight down one month file.

## Before making this public

- **Check your commit email**: `git log --format='%an <%ae>'`. If it shows a
  real personal email, switch to GitHub's private noreply address
  (Settings → Emails → "Keep my email addresses private") before flipping
  visibility — public commit history exposes whatever email is in it, forever.
- **Never commit real WiFi credentials or API tokens.** Put them in
  `secrets.h` / `.env` (already gitignored) and reference them from code
  instead of hardcoding — this matters starting Month 2 (ESP32 WiFi) and
  Month 6 (Hugging Face token for pushing to the LeRobot Hub).
- **Don't commit large binaries directly** — videos, ROS bags, big CAD
  exports. Link videos externally (unlisted YouTube works well) and use
  [Git LFS](https://git-lfs.com/) for anything sizeable you do want tracked;
  GitHub hard-caps individual files at 100MB.
- **Strip photo/video metadata** if it might contain GPS location (most
  phone cameras geotag by default) — check your OS's share/export settings
  before uploading build photos.
- A `LICENSE` (MIT) is included so it's clear the repo's content can be
  reused — remove or change it if you'd rather keep all rights reserved.

## Source

Based on the full roadmap article (checked against vendor/official docs,
September 2026). Refer back to it for the actual resource links — this
tracker just turns it into checkable daily units.
