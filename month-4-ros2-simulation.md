# Month 4 — ROS 2, Simulation, and Building Robots the Company Way

Goal: a robot in ROS 2, simulated, that maps a room and navigates it autonomously.
All of this month can run on a normal laptop, no GPU required.

⚠️ Use **ROS 2 Jazzy**, not ROS 1. If a tutorial types `catkin_make`, `roscore`,
`rosrun`, `rospy`, or XML-only launch files, close the tab — it's dead content.

## Week 1 — ROS 2 core concepts

- [ ] Day 1 — Install ROS 2 Jazzy; [official tutorials](https://docs.ros.org/en/jazzy/Tutorials.html): first node, publisher/subscriber (Python)
- [ ] Day 2 — Services: write a client + server pair
- [ ] Day 3 — Actions: write a simple action server + client with feedback
- [ ] Day 4 — Custom .msg and .srv definitions in your own package
- [ ] Day 5 — Parameters + YAML config files
- [ ] Day 6 — Launch files in Python: pass arguments, remap topics
- [ ] Day 7 — colcon workspace structure; ros2 bag record + replay. Alt course: [The Construct](https://www.theconstruct.ai/) (free tier, 3 courses) or [Edouard Renard ROS 2 for Beginners L1](https://www.udemy.com/course/ros2-for-beginners/) (~$10–20) — **Week 1 checkpoint**

## Week 2 — The no-hardware capstone + URDF/TF

- [ ] Day 8 — Build the multi-node system: sensor publisher → processing node → service-based config node → parameterised aggregator, custom msgs, one Python launch file — push to GitHub. Reference: [Articulated Robotics](https://articulatedrobotics.xyz/tutorials/), [MOGI-ROS course](https://github.com/orgs/MOGI-ROS/repositories)
- [ ] Day 9 — [Articulated Robotics: coordinate transforms series](https://articulatedrobotics.xyz/category/coordinate-transforms-for-robotics), part 1
- [ ] Day 10 — Coordinate transforms series, part 2 — get comfortable with frames before touching URDF
- [ ] Day 11 — Write a basic xacro file for a simple robot; understand joint_state_publisher vs robot_state_publisher (know the difference cold). Reference: [Official URDF tutorial](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher-cpp.html) or [Edouard Renard L2](https://www.udemy.com/course/ros2-tf-urdf-rviz-gazebo/)
- [ ] Day 12 — Design your own robot in xacro: diff-drive base + sensor mast + 2-DOF pan-tilt head
- [ ] Day 13 — Add correct inertial tags, separate collision/visual geometry
- [ ] Day 14 — Drive joints with joint_state_publisher_gui, view full TF tree in RViz, screenshot it — **Week 2 checkpoint**

## Week 3 — Simulation and ros2_control

- [ ] Day 15 — [Gazebo docs](https://gazebosim.org/docs/latest/getstarted/): spawn your xacro robot into Gazebo (Jazzy pairs with Gazebo Harmonic)
- [ ] Day 16 — Add a lidar plugin, confirm data appears on a ROS 2 topic and renders in RViz
- [ ] Day 17 — Add a camera plugin, same confirmation
- [ ] Day 18 — Build a custom SDF world with obstacles
- [ ] Day 19 — [ros2_control docs](https://control.ros.org/rolling/index.html): add `<ros2_control>` tags to your xacro
- [ ] Day 20 — Configure diff_drive_controller + joint_state_broadcaster via YAML, drive with keyboard teleop. Reference: [Articulated Robotics: ros2_control on real hardware](https://articulatedrobotics.xyz/tutorials/mobile-robot/applications/ros2_control-real/)
- [ ] Day 21 — Write an action server that drives a commanded distance with feedback + cancellation — **Week 3 checkpoint, push to GitHub**

## Week 4 — SLAM and Nav2

- [ ] Day 22 — [Nav2 Getting Started](https://docs.nav2.org/rolling/getting_started/index.html): launch it in simulation using the dev container
- [ ] Day 23 — [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox): run it in your Gazebo world, teleop around, save the map
- [ ] Day 24 — Switch SLAM Toolbox to localization mode, send Nav2 goals from RViz ([Nav2 Tutorials](https://docs.nav2.org/rolling/tutorials/))
- [ ] Day 25 — Costmap tuning: inflation radius, obstacle layers, local vs global split — fix corner-clipping
- [ ] Day 26 — Nav2 tutorials: read the behaviour-tree architecture, understand how Nav2 orchestrates planning
- [ ] Day 27 — Deliberately break the TF tree (remove a static transform), diagnose it, fix it — document in `logs/`
- [ ] Day 28 — Full run: robot builds its own map, then autonomously navigates it — screen-record for the portfolio, push to GitHub — **Month 4 milestone**

Optional real-hardware path (not required — sim covers the whole month):
[RPLIDAR C1](https://www.dfrobot.com/) $69 + Raspberry Pi + diff-drive base (~$250–450 DIY), or a ready platform like [Hiwonder MentorPi M1](https://www.hiwonder.com/products/mentorpi-m1) (from $299.99) or [Waveshare UGV Rover ROS 2 kit](https://www.waveshare.com/ugv-rover-ros2-kit.htm) ($534.99). Also worth knowing: [RTAB-Map](https://github.com/introlab/rtabmap_ros) for RGB-D/stereo SLAM if you have a depth camera instead of a lidar.

### Month 4 Milestone check
- [ ] Can write ROS 2 nodes in Python using topics, services, and actions
- [ ] Can describe your own robot in xacro with correct frames, inertias, collision geometry
- [ ] Can simulate that robot in Gazebo with working lidar and camera
- [ ] Can configure ros2_control and drive the robot through a controller
- [ ] Can build a map with SLAM Toolbox and navigate autonomously with Nav2
- [ ] Can diagnose a broken TF tree
