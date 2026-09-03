#!/usr/bin/env python3
"""
Progress tracker for the robotics roadmap.

Scans month-*.md for GitHub-style checkboxes and reports how many
"Day N" tasks are done vs total, per month and overall, plus your
current commit streak from git history.

Usage:
    python scripts/progress.py                   # print a table + streak
    python scripts/progress.py --badge PATH       # write a shields.io endpoint JSON badge to PATH
"""
import argparse
import glob
import json
import re
import subprocess
from datetime import date, timedelta
from pathlib import Path

DAY_RE = re.compile(r"^- \[( |x)\] Day (\d+)", re.IGNORECASE)
MILESTONE_RE = re.compile(r"^- \[( |x)\] (?!Day \d)")

MONTH_FILES = sorted(glob.glob("month-*.md"))


def parse_file(path):
    total_days = done_days = 0
    total_milestones = done_milestones = 0
    in_milestone_section = False
    for line in Path(path).read_text().splitlines():
        if line.startswith("### ") and "Milestone check" in line:
            in_milestone_section = True
            continue
        m = DAY_RE.match(line)
        if m:
            total_days += 1
            if m.group(1).lower() == "x":
                done_days += 1
            continue
        if in_milestone_section:
            mm = MILESTONE_RE.match(line)
            if mm:
                total_milestones += 1
                if mm.group(1).lower() == "x":
                    done_milestones += 1
    return total_days, done_days, total_milestones, done_milestones


def get_commit_dates():
    try:
        out = subprocess.run(
            ["git", "log", "--format=%ad", "--date=short"],
            capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return []
    return sorted(set(out.split()))


def current_streak(dates):
    if not dates:
        return 0
    parsed = sorted({date.fromisoformat(d) for d in dates}, reverse=True)
    streak = 1
    for i in range(1, len(parsed)):
        if parsed[i - 1] - parsed[i] == timedelta(days=1):
            streak += 1
        else:
            break
    return streak


def badge_color(pct):
    if pct >= 90:
        return "brightgreen"
    if pct >= 75:
        return "green"
    if pct >= 50:
        return "yellow"
    if pct >= 25:
        return "orange"
    return "red"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--badge", help="write a shields.io endpoint JSON badge to this path instead of printing")
    args = parser.parse_args()

    grand_total = grand_done = 0
    rows = []
    for f in MONTH_FILES:
        total, done, mtotal, mdone = parse_file(f)
        grand_total += total
        grand_done += done
        pct = (done / total * 100) if total else 0
        rows.append((f, done, total, pct, mdone, mtotal))

    overall_pct = (grand_done / grand_total * 100) if grand_total else 0

    if args.badge:
        payload = {
            "schemaVersion": 1,
            "label": "roadmap progress",
            "message": f"{grand_done}/{grand_total} days ({overall_pct:.0f}%)",
            "color": badge_color(overall_pct),
        }
        out_path = Path(args.badge)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, indent=2) + "\n")
        print(f"Wrote badge JSON to {out_path}: {payload['message']}")
        return

    print(f"{'File':38} {'Days':>10} {'%':>7}   Milestones")
    print("-" * 72)
    for f, done, total, pct, mdone, mtotal in rows:
        print(f"{f:38} {done:>4}/{total:<5} {pct:6.1f}%   {mdone}/{mtotal}")
    print("-" * 72)
    print(f"{'TOTAL':38} {grand_done:>4}/{grand_total:<5} {overall_pct:6.1f}%")

    dates = get_commit_dates()
    streak = current_streak(dates)
    print(f"\nCurrent commit streak: {streak} day(s)")
    print(f"Total distinct days with a commit: {len(dates)}")


if __name__ == "__main__":
    main()
