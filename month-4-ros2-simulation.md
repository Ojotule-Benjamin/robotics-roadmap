# Month 4 — ROS 2, Simulation, and Building Robots the Company Way

Goal: a robot in ROS 2, simulated, that maps a room and navigates it autonomously.
All of this month can run on a normal laptop, no GPU required.

## Week 1 — ROS 2 core concepts (Jazzy — not ROS 1, watch for catkin_make/roscore/rospy = dead tutorial)

- [ ] Day 1 — Install ROS 2 Jazzy; official tutorials: first node, publisher/subscriber (Python)
- [ ] Day 2 — Services: write a client + server pair
- [ ] Day 3 — Actions: write a simple action server + client with feedback
- [ ] Day 4 — Custom .msg and .srv definitions in your own package
- [ ] Day 5 — Parameters + YAML config files
- [ ] Day 6 — Launch files in Python: pass arguments, remap topics
- [ ] Day 7 — colcon workspace structure; ros2 bag record + replay — **Week 1 checkpoint**

## Week 2 — The no-hardware capstone + URDF/TF

- [ ] Day 8 — Build the multi-node system: sensor publisher → processing node → service-based config node → parameterised aggregator, custom msgs, one Python launch file — push to GitHub
- [ ] Day 9 — Articulated Robotics: coordinate transforms series, part 1
- [ ] Day 10 — Coordinate transforms series, part 2 — get comfortable with frames before touching URDF
- [ ] Day 11 — Write a basic xacro file for a simple robot; understand joint_state_publisher vs robot_state_publisher (know the difference cold)
- [ ] Day 12 — Design your own robot in xacro: diff-drive base + sensor mast + 2-DOF pan-tilt head
- [ ] Day 13 — Add correct inertial tags, separate collision/visual geometry
- [ ] Day 14 — Drive joints with joint_state_publisher_gui, view full TF tree in RViz, screenshot it — **Week 2 checkpoint**

## Week 3 — Simulation and ros2_control

- [ ] Day 15 — Gazebo docs: spawn your xacro robot into Gazebo
- [ ] Day 16 — Add a lidar plugin, confirm data appears on a ROS 2 topic and renders in RViz
- [ ] Day 17 — Add a camera plugin, same confirmation
- [ ] Day 18 — Build a custom SDF world with obstacles
- [ ] Day 19 — ros2_control docs: add `<ros2_control>` tags to your xacro
- [ ] Day 20 — Configure diff_drive_controller + joint_state_broadcaster via YAML, drive with keyboard teleop
- [ ] Day 21 — Write an action server that drives a commanded distance with feedback + cancellation — **Week 3 checkpoint, push to GitHub**

## Week 4 — SLAM and Nav2

- [ ] Day 22 — Nav2 "Getting Started": launch it in simulation using the dev container
- [ ] Day 23 — SLAM Toolbox: run it in your Gazebo world, teleop around, save the map
- [ ] Day 24 — Switch SLAM Toolbox to localization mode, send Nav2 goals from RViz
- [ ] Day 25 — Costmap tuning: inflation radius, obstacle layers, local vs global split — fix corner-clipping
- [ ] Day 26 — Nav2 tutorials: read the behaviour-tree architecture, understand how Nav2 orchestrates planning
- [ ] Day 27 — Deliberately break the TF tree (remove a static transform), diagnose it, fix it — document in `logs/`
- [ ] Day 28 — Full run: robot builds its own map, then autonomously navigates it — screen-record for the portfolio, push to GitHub — **Month 4 milestone**

### Month 4 Milestone check
- [ ] Can write ROS 2 nodes in Python using topics, services, and actions
- [ ] Can describe your own robot in xacro with correct frames, inertias, collision geometry
- [ ] Can simulate that robot in Gazebo with working lidar and camera
- [ ] Can configure ros2_control and drive the robot through a controller
- [ ] Can build a map with SLAM Toolbox and navigate autonomously with Nav2
- [ ] Can diagnose a broken TF tree
