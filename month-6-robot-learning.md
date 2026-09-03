# Month 6 — Robot Learning, Specialisation, Becoming Hireable

Goal: pick one direction, build a portfolio piece in it, start applying.

## Week 1 — LeRobot: teleoperate, record, train, deploy

- [ ] Day 1 — Hugging Face Robotics Course, units 0–1 (runs in sim, no hardware needed)
- [ ] Day 2 — LeRobot docs: understand the full record→train→deploy pipeline
- [ ] Day 3 — SO-101 LeRobot setup guide: port-finding, motor setup, calibration for recording
- [ ] Day 4 — Record 15 demonstrations of a single simple task (e.g. pick cube, drop in bin)
- [ ] Day 5 — Record 35 more (50 total); review dataset quality, remove bad episodes
- [ ] Day 6 — Train an ACT policy on the 50-episode dataset
- [ ] Day 7 — Deploy the policy on the real arm, measure success rate over N trials — **Week 1 checkpoint**

## Week 2 — Iterate on the policy + survey the VLA landscape

- [ ] Day 8 — Identify failure modes from Week 1's runs
- [ ] Day 9 — Record 50 more demonstrations specifically covering those failure cases
- [ ] Day 10 — Retrain, redeploy, measure success rate again — document before/after numbers
- [ ] Day 11 — Read ACT paper/docs section: why predicting action chunks beats single-step prediction
- [ ] Day 12 — Read Diffusion Policy overview: denoising-process framing, reported gains
- [ ] Day 13 — Survey open VLAs: OpenVLA, π₀/π₀-FAST, GR00T N1.7, SmolVLA — note license, size, VRAM needs for each
- [ ] Day 14 — Write a one-page comparison of the VLAs surveyed — **Week 2 checkpoint, push dataset + policy + comparison to GitHub/LeRobot Hub**

## Week 3 — Reinforcement learning for robotics

- [ ] Day 15 — MuJoCo Playground: run the first Colab tutorial (locomotion)
- [ ] Day 16 — MuJoCo Playground: second tutorial (manipulation or vision task)
- [ ] Day 17 — Train a quadruped locomotion policy from a Colab tutorial
- [ ] Day 18 — Modify the reward function, observe how the gait changes, document it
- [ ] Day 19 — CS 285 (Levine): watch the imitation learning + policy gradient lectures
- [ ] Day 20 — Write a short note connecting what you just did (RL) to what you did in Week 1 (imitation learning) — when would you reach for each?
- [ ] Day 21 — Push the RL experiment + writeup to GitHub — **Week 3 checkpoint**

## Week 4 — Pick a direction + build the portfolio

- [ ] Day 22 — Decide: Robot Learning / Autonomy & Mobile Robotics / Embedded & Mechatronics — write one paragraph on why
- [ ] Day 23 — Pick your 3 strongest projects from the last 6 months
- [ ] Day 24 — Rewrite README #1: video at top, architecture/wiring diagram, real measured numbers, "what broke" section
- [ ] Day 25 — Rewrite README #2, same structure
- [ ] Day 26 — Rewrite README #3, same structure
- [ ] Day 27 — Pick one open-source project in your chosen direction (Nav2 / LeRobot / MoveIt / Isaac Lab) and find a small real issue to contribute to
- [ ] Day 28 — Submit that contribution (even a docs fix or small bug report counts as a start)

## Week 5 — Interview prep

- [ ] Day 29 — Review PID, sensor fusion/Kalman, SLAM concepts, RRT/path planning — write short answers to each from memory
- [ ] Day 30 — Have someone interrogate you about one of your own repos for 20 minutes — specific code, not concepts. If you can't answer 3 levels deep, go fix that project first
- [ ] Day 31 — Repeat the interrogation on repo #2
- [ ] Day 32 — Repeat on repo #3; update `logs/` with anything you couldn't answer well
- [ ] Day 33 — Start applying: technician roles, teleoperation/data-collection roles, or direct outreach to small robotics startups — **Month 6 milestone**

### Month 6 Milestone check
- [ ] Recorded a demonstration dataset and trained a policy that runs on your own hardware
- [ ] Can explain the difference between behaviour cloning, ACT, and diffusion policy
- [ ] Can name which VLA models have open weights and which don't
- [ ] Have stated which of the three directions you're pursuing, and why
- [ ] Three portfolio projects with video, metrics, and a documented failure analysis
- [ ] Can answer three levels of follow-up questions about any line of your own code
