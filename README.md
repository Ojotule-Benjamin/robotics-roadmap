# Robotics Roadmap — 6 Month Tracker

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
├── logs/
│   ├── TEMPLATE.md
│   └── day-XXX.md   (one per failure worth documenting)
└── projects/
    └── (each build gets its own folder: code, wiring notes, photos/video links)
```

`RESOURCES.md` and `SHOPPING-LIST.md` make the repo self-contained — you
shouldn't need to go back to the original article to find a link or a price
once you're working from this tracker.

## Source

Based on the full roadmap article (checked against vendor/official docs,
September 2026). Refer back to it for the actual resource links — this
tracker just turns it into checkable daily units.
