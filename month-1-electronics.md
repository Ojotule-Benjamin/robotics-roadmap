# Month 1 — Electronics, the Bench, and the Tools

Goal: read a schematic, build a circuit that works, find the fault when it doesn't.

## Week 1 — Electronics fundamentals (simulator-first, spend $0)

- [ ] Day 1 — [Falstad Circuit Simulator](https://www.falstad.com/circuit/): build a simple series circuit, watch current flow, confirm Ohm's law (V=IR) by hand vs sim
- [ ] Day 2 — Falstad: build a voltage divider, calculate output voltage by hand, verify in sim
- [ ] Day 3 — [Tinkercad Circuits](https://www.tinkercad.com/circuits): recreate the divider on a virtual breadboard with a virtual multimeter
- [ ] Day 4 — [All About Circuits](https://www.allaboutcircuits.com/textbook/): read capacitors + transistors chapters; note what a transistor switch does
- [ ] Day 5 — Falstad: build a transistor switch — logic-level input turning on an LED — this is the exact circuit for driving high-current loads from a 3.3V pin
- [ ] Day 6 — [Afrotechmods](https://afrotechmods.com/tutorials/): watch pull-up/pull-down resistor videos; sketch both configurations from memory
- [ ] Day 7 — Review + quiz yourself: Ohm's law, dividers, pull-up/down, decoupling caps, LiPo cell count/C rating basics — **Week 1 checkpoint**

Optional deep dive: [Make: Electronics, 3rd ed. — Charles Platt](https://www.makershed.com/products/make-electronics-3rd-edition-print) ($29.99) if you want a paper book alongside the free resources above.

## Week 2 — The bench: order kit, start hands-on measurement

- [ ] Day 8 — Decide your budget tier and order. Pick one:
  - [Elegoo UNO R3 Super Starter Kit](https://www.elegoo.com/products/elegoo-uno-r3-super-starter-kit) — $42.99 (best value, 22-lesson PDF)
  - [Elegoo UNO Basic Starter Kit](https://www.elegoo.com/products/elegoo-uno-basic-starter-kit) — $19.99 (cheapest real entry point)
  - [SparkFun Inventor's Kit v4.1.2](https://www.sparkfun.com/sparkfun-inventor-s-kit-v4-1-2.html) — $99.95 (best curriculum)
  - Also get: [Adafruit multimeter 9205B+](https://www.adafruit.com/product/2034) — $17.50, and [Pinecil V2 soldering iron](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/) — $25.99–35.99
  - Buy from Amazon or Elegoo direct for speed on this first order — switch to AliExpress later once you know what you need
- [ ] Day 9 — While waiting on shipping: All About Circuits — schematic symbol reference (resistor, cap, diode, transistor, ground, Vcc)
- [ ] Day 10 — Kit arrives: unbox, identify every component against the schematic legend
- [ ] Day 11 — Multimeter: measure battery voltage, measure resistance of 5 resistors, check against color bands
- [ ] Day 12 — Multimeter: continuity mode — deliberately break a wire, find the break
- [ ] Day 13 — Build the physical voltage divider from Day 2 on a real breadboard, measure output, compare to calculated value
- [ ] Day 14 — Build the transistor-switch LED circuit from Day 5 on real hardware — **Week 2 checkpoint**

## Week 3 — Soldering

- [ ] Day 15 — [Adafruit Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering): read in full, note the photos of bad joints
- [ ] Day 16 — Practice: tin the iron tip, practice heating a joint (not the solder) on scrap wire
- [ ] Day 17 — Solder header pins onto a cheap breakout board
- [ ] Day 18 — Continuity-test every soldered pin; identify and fix any cold joints
- [ ] Day 19 — Desolder one pin, resolder it cleanly — repeat the whole board 2 more times
- [ ] Day 20 — [SparkFun "How to Use a Multimeter"](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter): read the fuse-blowing section, know what to do if it happens — **Week 3 checkpoint**

## Week 4 — Python, terminal, Git

- [ ] Day 21 — [CS50P](https://cs50.harvard.edu/python/) or [Python for Everybody](https://www.coursera.org/specializations/python): functions + control flow (pick one course and commit to it)
- [ ] Day 22 — Python: file I/O, JSON, virtual environments, pip
- [ ] Day 23 — [Missing Semester (MIT)](https://missing.csail.mit.edu/): shell basics — cd, ls, grep, running scripts
- [ ] Day 24 — Missing Semester: environment variables, ssh basics
- [ ] Day 25 — [Learn Git Branching](https://learngitbranching.js.org/): init, add, commit, push
- [ ] Day 26 — Learn Git Branching: branches and merges
- [ ] Day 27 — Create this repo (or your own), write a README with a photo + wiring description template for future projects
- [ ] Day 28 — Push a small Python script (e.g. a resistor color-code calculator) to GitHub with a proper README — **Month 1 milestone**

### Month 1 Milestone check
- [ ] Can read a schematic and build the circuit it describes
- [ ] Can calculate a resistor value before plugging it in
- [ ] Can find a short/break/dead component with a multimeter
- [ ] Can solder a clean through-hole joint and verify it electrically
- [ ] Can write a Python script, run it from terminal, push it to GitHub
- [ ] Can explain out loud why a stalling motor can reset a microcontroller
