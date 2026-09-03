# Month 3 — Mechanical Design, CAD, and Manufacturing

Goal: design a part in CAD, manufacture it, have it fit.

## Week 1 — CAD fundamentals

- [ ] Day 1 — Pick your tool (Onshape / Fusion / FreeCAD / SOLIDWORKS for Makers) and commit — don't sample all four
- [ ] Day 2 — Fundamentals course, part 1: sketching basics
- [ ] Day 3 — Fundamentals course, part 2: fully-constrained sketches (deliberately leave one under-constrained, edit it, watch it move — learn why this matters)
- [ ] Day 4 — Parametric design: build a part driven entirely by variables, change one dimension, watch the whole part update
- [ ] Day 5 — Assemblies and mates: revolute, slider, fixed — build a simple 2-part hinge assembly
- [ ] Day 6 — Read Protolabs "Design for 3D printing" guide: wall thickness, orientation, tolerances, snap-fits
- [ ] Day 7 — Pull the datasheet drawing for a servo you own; model a bracket around its exact hole spacing — **Week 1 checkpoint**

## Week 2 — 3D printing setup and calibration

- [ ] Day 8 — Get printer access (own one / library makerspace / Fab Lab / print service) — decide which
- [ ] Day 9 — OrcaSlicer calibration wiki: temperature tower
- [ ] Day 10 — Calibration: flow rate + pressure advance
- [ ] Day 11 — Calibration: retraction tuning
- [ ] Day 12 — Print the Clearance and Tolerance gauge; record your machine's real clearance numbers
- [ ] Day 13 — Print the Day 7 servo bracket; note where it doesn't fit and why
- [ ] Day 14 — Redesign and reprint the bracket until it fits correctly — **Week 2 checkpoint**

## Week 3 — Materials, iteration, transmissions

- [ ] Day 15 — Read CNC Kitchen strength-test summaries: infill, walls, orientation as data not folklore
- [ ] Day 16 — Design a two-part snap-fit enclosure for your ESP32
- [ ] Day 17 — Print + iterate the enclosure until it clicks shut without glue
- [ ] Day 18 — Learn gear ratios, backlash, belt vs gear vs direct drive (concepts only)
- [ ] Day 19 — Design a simple planetary or cycloidal reducer for a NEMA17/hobby motor (reference: Instructables OpenCycloid)
- [ ] Day 20 — Print it, measure backlash by hand, redesign to reduce it — **Week 3 checkpoint**

## Week 4 — Build the SO-101 arm

- [ ] Day 21 — Order SO-101 kit (or cheaper alternative — see article's budget tiers) and print parts if needed
- [ ] Day 22 — Assemble arm structure, mount servos
- [ ] Day 23 — Calibrate every servo per the LeRobot SO-101 setup guide
- [ ] Day 24 — Assemble the leader/follower pair (or single follower if budget-limited)
- [ ] Day 25 — Teleoperate: hand-guide the leader, confirm the follower mirrors it correctly
- [ ] Day 26 — Design custom gripper fingers in CAD (TPU) to replace the stock ones
- [ ] Day 27 — Print the custom fingers, mount them
- [ ] Day 28 — Test the custom gripper on 3 objects of different shapes/sizes, film it
- [ ] Day 29 — Push arm build to GitHub: assembly notes, calibration steps, gripper CAD files, video, "what broke" log — **Month 3 milestone**

### Month 3 Milestone check
- [ ] Can model a part from a datasheet in CAD with fully constrained sketches
- [ ] Know your printer's real clearance numbers from measurement, not guesswork
- [ ] Can design a part specifically for FDM (orientation, overhangs, layer adhesion)
- [ ] Can choose PLA/PETG/ABS/TPU for a given part and justify it
- [ ] Can explain backlash and demonstrate it on something you built
- [ ] Working robot arm assembled, calibrated, and modified with your own parts, on GitHub
