# Month 5 — The Math That Makes Robots Actually Work

Goal: understand and implement the control and perception underneath everything built so far.

## Week 1 — Control theory / PID from first principles

- [ ] Day 1 — [MATLAB Tech Talks "Understanding PID Control"](https://www.mathworks.com/videos/series/understanding-pid-control.html): parts 1–3
- [ ] Day 2 — Parts 4–7: integrator windup, derivative filtering, tuning methods
- [ ] Day 3 — Implement P-only control on the Month-2 balancer, log step response to CSV
- [ ] Day 4 — Add the D term (PD), log step response
- [ ] Day 5 — Add I with feedforward (full PID+FF), log step response
- [ ] Day 6 — Plot all three step responses together; write up which you'd ship and why
- [ ] Day 7 — Push the PID comparison (code + plots + writeup) to GitHub. Alt/deeper resource: [Brian Douglas Control System Lectures](https://www.youtube.com/@BrianBDouglas/playlists), [free companion book](https://engineeringmedia.com/books) — **Week 1 checkpoint**

## Week 2 — State space, LQR, MPC

- [ ] Day 8 — [Steve Brunton Control Bootcamp](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m): state space representation basics
- [ ] Day 9 — Control Bootcamp: controllability and observability
- [ ] Day 10 — [Tedrake's Underactuated Robotics](https://underactuated.csail.mit.edu/index.html): cart-pole chapter — get the model
- [ ] Day 11 — Implement LQR for the simulated cart-pole in Python
- [ ] Day 12 — Implement hand-tuned PID for the same cart-pole, compare disturbance rejection
- [ ] Day 13 — [MATLAB Tech Talks "Understanding MPC"](https://www.mathworks.com/videos/series/understanding-model-predictive-control.html): parts 1–4 — what MPC buys you (constraints) vs costs (compute)
- [ ] Day 14 — Write up the LQR vs PID comparison. Rigorous reference: [Feedback Systems — Åström & Murray (free PDF)](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers) — **Week 2 checkpoint**

## Week 3 — Kinematics and dynamics

- [ ] Day 15 — [Modern Robotics — Kevin Lynch](http://hades.mech.northwestern.edu/index.php/Modern_Robotics): homogeneous transforms chapter (or the [Coursera specialization](https://www.coursera.org/specializations/modernrobotics) if you want structure/deadlines)
- [ ] Day 16 — Forward kinematics: compute your SO-101's FK by hand from link lengths
- [ ] Day 17 — Verify your hand-computed FK against the [Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python)
- [ ] Day 18 — The Jacobian: what it means physically, what a singularity is. Short-lesson reference: [QUT Robot Academy](https://robotacademy.net.au)
- [ ] Day 19 — Write a numerical IK solver that moves the SO-101 end effector to a commanded XYZ
- [ ] Day 20 — Drive the arm near a singularity deliberately, observe/document what happens
- [ ] Day 21 — Trajectory generation: joint-space vs Cartesian-space interpolation, implement both for a simple move — **Week 3 checkpoint**

## Week 4 — Perception / computer vision

- [ ] Day 22 — [OpenCV Bootcamp](https://courses.opencv.org/courses/course-v1:OpenCV+Bootcamp+CV0/about): image manipulation + filtering modules
- [ ] Day 23 — OpenCV Bootcamp: edge detection + tracking modules
- [ ] Day 24 — Camera calibration: print a chessboard, run the [official OpenCV calibration tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html), save intrinsics
- [ ] Day 25 — Pinhole projection: understand image coords vs world coords; write a script detecting a colored object
- [ ] Day 26 — Estimate the object's 3D position relative to the camera using your calibration
- [ ] Day 27 — Change the lighting, watch the pipeline fail, fix it, document in `logs/`
- [ ] Day 28 — [Open3D point cloud tutorials](https://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html): voxel downsampling, plane fitting to find a table surface. Deeper geometry reference: [Cyrill Stachniss lectures](https://www.ipb.uni-bonn.de/online-training-robotics/) — **Week 4 checkpoint**

## Week 5 — Manipulation with MoveIt 2

- [ ] Day 29 — [MoveIt 2 "Getting Started"](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html): plan motions for a simulated arm
- [ ] Day 30 — Add collision objects to the planning scene
- [ ] Day 31 — Execute a full pick-and-place using [MoveIt Task Constructor](https://moveit.picknik.ai/main/doc/tutorials/pick_and_place_with_moveit_task_constructor/pick_and_place_with_moveit_task_constructor.html)
- [ ] Day 32 — Deliberately block the only viable path, observe planner failure behavior, document it. Deeper reference: [Robotic Manipulation — Tedrake](https://manipulation.csail.mit.edu/), [Contact-GraspNet](https://github.com/NVlabs/contact_graspnet) for learned grasping
- [ ] Day 33 — Push the full month's work (PID plots, LQR comparison, FK/IK code, calibration + vision script, MoveIt pick-and-place) to GitHub — **Month 5 milestone**

### Month 5 Milestone check
- [ ] Can implement and tune PID, explain every term from measured data
- [ ] Can describe a system in state space and implement LQR on a simulated plant
- [ ] Can compute forward kinematics by hand and solve IK numerically
- [ ] Can explain a singularity by pointing at a robot doing it
- [ ] Can calibrate a camera and turn a pixel into a 3D position
- [ ] Can plan and execute a collision-free pick-and-place in MoveIt 2
