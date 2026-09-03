# Month 3 — Mechanical Design, CAD, and Manufacturing

Goal: design a part in CAD, manufacture it, have it fit.

## Week 1 — CAD fundamentals

- [ ] Day 1 — Pick your tool and commit — don't sample all four:
  - [Onshape Fundamentals: CAD](https://learn.onshape.com/learning-paths/onshape-fundamentals-cad) — free, browser-based, public docs on free tier
  - [Learn Fusion in 30 Days](https://productdesignonline.com/learn-autodesk-fusion-360-in-30-days-official-course/) — free on 3-yr renewable non-commercial term
  - [MangoJelly FreeCAD tutorials](https://www.youtube.com/@MangoJellySolutions) — free, no licensing catch, v1.1 (Mar 2026) is genuinely usable
  - SOLIDWORKS for Makers — $48/yr, native files watermarked
- [ ] Day 2 — Fundamentals course, part 1: sketching basics
- [ ] Day 3 — Fundamentals course, part 2: fully-constrained sketches (deliberately leave one under-constrained, edit it, watch it move — learn why this matters)
- [ ] Day 4 — Parametric design: build a part driven entirely by variables, change one dimension, watch the whole part update
- [ ] Day 5 — Assemblies and mates: revolute, slider, fixed — build a simple 2-part hinge assembly
- [ ] Day 6 — Read [Protolabs "Design for 3D printing"](https://www.hubs.com/knowledge-base/design-for-3d-printing/) guide: wall thickness, orientation, tolerances, snap-fits
- [ ] Day 7 — Pull the datasheet drawing for a servo you own; model a bracket around its exact hole spacing — **Week 1 checkpoint**

## Week 2 — 3D printing setup and calibration

- [ ] Day 8 — Get printer access — decide which:
  - Own one: [Creality Ender-3 V3 SE](https://store.creality.com/products/ender-3-v3-se-3d-printer) $199 / [Bambu A1 mini](https://www.bestbuy.com/product/bambu-lab-a1-mini-3d-printer-silver/CZTZV9ZGGV) $219.99 / [Bambu A1](https://www.bestbuy.com/product/bambu-lab-a1-3d-printer-silver/CZW2ZH33H4) $299.99
  - No printer: [Fab Labs directory](https://fablabs.io/labs), [library makerspaces](https://action.everylibrary.org/how_to_find_a_makerspace_near_you), [Craftcloud](https://craftcloud3d.com/), [JLC3DP](https://jlc3dp.com/) (from $1/part)
- [ ] Day 9 — [OrcaSlicer calibration wiki](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration): temperature tower
- [ ] Day 10 — Calibration: flow rate + pressure advance
- [ ] Day 11 — Calibration: retraction tuning ([Teaching Tech interactive walkthrough](https://teachingtechyt.github.io/calibration.html) as backup reference)
- [ ] Day 12 — Print the [Clearance and Tolerance gauge](https://www.printables.com/model/57067-clearance-and-tolerance-3d-printer-gauge); record your machine's real clearance numbers
- [ ] Day 13 — Print the Day 7 servo bracket; note where it doesn't fit and why
- [ ] Day 14 — Redesign and reprint the bracket until it fits correctly — **Week 2 checkpoint**

## Week 3 — Materials, iteration, transmissions

- [ ] Day 15 — Read [CNC Kitchen](https://www.youtube.com/@CNCKitchen) strength-test summaries: infill, walls, orientation as data not folklore
- [ ] Day 16 — Design a two-part snap-fit enclosure for your ESP32
- [ ] Day 17 — Print + iterate the enclosure until it clicks shut without glue (PETG recommended for toughness)
- [ ] Day 18 — Learn gear ratios, backlash, belt vs gear vs direct drive (concepts only)
- [ ] Day 19 — Design a simple planetary or cycloidal reducer for a NEMA17/hobby motor. Reference: [OpenCycloid on Instructables](https://www.instructables.com/OpenCycloid-3D-printed-Open-Source-Robotic-Actuato/)
- [ ] Day 20 — Print it, measure backlash by hand, redesign to reduce it — **Week 3 checkpoint**

## Week 4 — Build the SO-101 arm

- [ ] Day 21 — Order the arm and print parts if needed:
  - [Official SO-ARM100 repo/BOM](https://github.com/TheRobotStudio/SO-ARM100) — pair $229.88, single follower $121.94 (excl. printing)
  - [Seeed SO-ARM101 Pro servo kit](https://www.seeedstudio.com/SO-ARM101-Low-Cost-AI-Arm-Kit-Pro-p-6427.html) $277.99 + [printed parts set](https://www.seeedstudio.com/SO-ARM101-3D-printed-Enclosure-p-6428.html) $30.99 if you have no printer
  - Budget alternative: [EEZYbotARM MK2](https://www.thingiverse.com/thing:1454048) (free STLs, $50–80) or [Hiwonder xArm 1S](https://www.hiwonder.com/products/xarm-1s) ($199.99)
- [ ] Day 22 — Assemble arm structure, mount servos
- [ ] Day 23 — Calibrate every servo per the [LeRobot SO-101 setup guide](https://huggingface.co/docs/lerobot/so101)
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
