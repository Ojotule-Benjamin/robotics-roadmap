# Shopping List — Everything You'll Need to Buy

All prices as verified against vendor pages, September 2026. Prices and
stock change — treat these as the ballpark, not gospel, and recheck before
ordering anything expensive.

## Where to order from, generally

| Vendor | Speed | Price | Best for |
|---|---|---|---|
| AliExpress | 2–6 weeks | Cheapest, often 3–10x less | Once you know exactly what you need |
| Amazon | Fast | Mid | Your **first** kit — pay the premium to start within days |
| Elegoo direct | ~1 week | Mid | Kits, ships from regional warehouses |
| Adafruit / SparkFun | Fast | Higher | Early on — every product page has a full tutorial + real support |
| Seeed Studio / DFRobot | Worldwide | Low-mid | General components |
| Pololu | International | Mid | Motors and drivers specifically — best source |
| DigiKey / Mouser | Fast | Varies | Exact parts by spec with real datasheets, not kits |

**For your very first order: buy from Amazon or Elegoo direct**, so you're
building within days instead of waiting a month. Once you know what a 10k
resistor is for, shift to AliExpress for the savings.

⚠️ **LiPo batteries**: never leave charging unattended, know your cell count
and C rating before buying/using one (covered in Month 1).

---

## Month 1 — Electronics & tools

Budget tiers (pick one, or step up as you go):

- **Tier 0 — $0**: Falstad + Tinkercad + All About Circuits. Do this first regardless of budget.
- **Tier 1 — ~$45–60**: starter kit + multimeter, all solderless, no iron needed yet.
- **Tier 2 — ~$110–160**: add a soldering iron, solder, side cutters, wire strippers, helping hands, perfboard, extra passives.
- **Tier 3 — ~$200–300**: add a bench power supply, better meter, desoldering pump, storage drawers, a robot chassis kit.

| Item | Price | Link |
|---|---|---|
| Elegoo UNO R3 Super Starter Kit (best value, 22-lesson PDF) | $42.99 | https://www.elegoo.com/products/elegoo-uno-r3-super-starter-kit |
| Elegoo UNO Basic Starter Kit (cheapest real entry point) | $19.99 | https://www.elegoo.com/products/elegoo-uno-basic-starter-kit |
| SparkFun Inventor's Kit v4.1.2 (best curriculum, 16 circuits/5 projects) | $99.95 | https://www.sparkfun.com/sparkfun-inventor-s-kit-v4-1-2.html |
| Adafruit digital multimeter 9205B+ | $17.50 | https://www.adafruit.com/product/2034 |
| Pinecil V2 soldering iron (temp-controlled, USB-C) | $25.99 (community) / $35.99 (retail) | https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/ |

Also buy separately as needed: solder, side cutters, wire strippers,
helping-hands stand, perfboard, an assortment of resistors/capacitors
(often included in kits above).

---

## Month 2 — Microcontrollers, motors, sensors

**Boards**

| Item | Price | Link |
|---|---|---|
| ESP32-S3-DevKitC-1, 8MB flash (main board — most capable current variant) | $15.95 | https://www.adafruit.com/product/5312 |
| Classic ESP32 Dev Board (for older tutorial code) | $15.00 | https://www.adafruit.com/product/3269 |
| Seeed XIAO ESP32-C3 (tiny form factor) | $4.99 | https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html |
| Generic ESP32 clones (AliExpress, unverified but well-known range) | ~$4–9 | search AliExpress |

**Motor drivers & motors**

| Item | Price | Link |
|---|---|---|
| Adafruit DRV8833 motor driver (cheapest good driver) | $5.95 | https://www.adafruit.com/product/3297 |
| SparkFun TB6612FNG breakout (correct default — better than L298N) | $14.77 | https://www.sparkfun.com/sparkfun-motor-driver-dual-tb6612fng-1a.html |
| Pololu gearmotor w/ encoder assembly | $19.95 each | https://www.pololu.com/product/3675 |
| Pololu A4988 stepper driver carrier | $8.95 | https://www.pololu.com/product/1182 |
| FeeTech STS3215 smart servo, 12V, 30 kg·cm (used in SO-101 arm) | $31.71 | https://www.robotshop.com/products/feetech-12v-30kgcm-magnetic-encoding-servo-sts3215 |

> ⚠️ The L298N shows up in every tutorial — learn it, then avoid it. It's an
> obsolete bipolar H-bridge that drops ~2V, runs hot, and wastes battery.
> Use the TB6612FNG or DRV8833 instead.

**Sensors**

| Item | Price |
|---|---|
| HC-SR04 ultrasonic (cheap, wide cone, poor on soft surfaces) | $3.95 |
| VL53L0X time-of-flight laser (narrow 35° cone, no double-imaging) | $14.95 |
| MPU-6050 6-DoF IMU (classic, you do the fusion yourself) | $12.95 |
| BNO085 9-DoF IMU (fusion on-chip, UART mode) | $29.50 |
| Pololu magnetic encoder pair (for odometry) | $8.95 |
| RPLIDAR C1 360° lidar (newer/cheaper than classic A1), DFRobot | $69.00 |

**Robot builds — bill of materials**

*Line-following robot*
- Quality build (~$105): ESP32-S3 $15.95 + Pololu Romi chassis kit $39.95 + TB6612FNG $14.77 + QTR-8RC reflectance array $12.95 + batteries/holder ~$12 + wiring/headers ~$10
- Budget build (~$38): generic ESP32 ~$6 + 2WD acrylic chassis ~$12 + DRV8833 $5.95 + 5x TCRT5000 sensors ~$3 + batteries ~$6 + wiring ~$5

*Self-balancing robot*
- Quality build (~$134): ESP32 $15.95 + 2x gearmotor-with-encoder $39.90 + TB6612FNG $14.77 + MPU-6050 $12.95 + printed/laser-cut chassis ~$10 + LiPo/charger/wheels ~$30 + misc ~$10
- Budget build (~$62): scale down proportionally using cheaper parts above

---

## Month 3 — CAD & manufacturing

**3D printers** (only buy if you don't have Fab Lab / library / print-service access)

| Item | Price | Link |
|---|---|---|
| Creality Ender-3 V3 SE | $199 | https://store.creality.com/products/ender-3-v3-se-3d-printer |
| Bambu Lab A1 mini | $219.99 | https://www.bestbuy.com/product/bambu-lab-a1-mini-3d-printer-silver/CZTZV9ZGGV |
| Bambu Lab A1 (256mm bed, for larger brackets) | $299.99 | https://www.bestbuy.com/product/bambu-lab-a1-3d-printer-silver/CZW2ZH33H4 |
| Creality K1C (enclosed, hardened for carbon-fiber filaments) | $369 | https://store.creality.com/products/k1c-3d-printer |
| Bambu Lab P1S (enclosed CoreXY, for ABS/ASA) | $799 | https://us.store.bambulab.com/products/p1s |

**No printer? Use instead:**
- Fab Labs worldwide (~2,875 labs): https://fablabs.io/labs
- Library makerspaces (US): https://action.everylibrary.org/how_to_find_a_makerspace_near_you
- Craftcloud (print-service quotes, 95 countries): https://craftcloud3d.com/
- JLC3DP (from $1.00/part, 3-day builds): https://jlc3dp.com/

**Filament — what to buy and why**

| Material | Use for | Notes |
|---|---|---|
| PLA / PLA+ | Prototype brackets, jigs, the SO-101 arm itself | Stiffest of the easy materials; creeps under load, softens ~55–60°C |
| PETG | Default "real" robot part — chassis plates, gearbox housings, servo mounts | Tough, better layer adhesion than PLA, stringy |
| ABS / ASA | Parts near hot motors, outdoor rovers | Warp badly without an enclosure |
| Nylon | Gears, cable guides | Easier to order printed than to print yourself |
| Carbon-fiber filled | Stiff structural links | Needs a hardened nozzle — abrasive |
| TPU | Feet, bumpers, compliant gripper fingers | Used for the SO-101's custom gripper fingers |

**SO-101 robot arm** (the Month 3 capstone build)

| Option | Price | Link |
|---|---|---|
| Official BOM (leader + follower pair, no printing) | $229.88 | https://github.com/TheRobotStudio/SO-ARM100 |
| Official BOM (single follower arm, no printing) | $121.94 | same repo |
| Seeed Studio SO-ARM101 Pro servo kit (motors + boards, no printed parts) | $277.99 | https://www.seeedstudio.com/SO-ARM101-Low-Cost-AI-Arm-Kit-Pro-p-6427.html |
| Seeed Studio printed parts set (if you have no printer) | $30.99 | https://www.seeedstudio.com/SO-ARM101-3D-printed-Enclosure-p-6428.html |
| Robonine SO-ARM101 complete kit (ships from Delaware) | $349.00 | https://robonine.com/shop/so-arm101-black-robotic-arm-kit/ |
| WowRobo via OpenELAB — printed+servos / unassembled / fully assembled | $325.99 / $419.99 / $489.99 | https://openelab.com/products/wowrobo-robotics-so-arm101-diykit |

**Cheaper arm alternatives at every tier**
- $0: LeRobot stack runs entirely in MuJoCo simulation, no hardware needed
- $50–80: EEZYbotARM MK2 — free STLs, built from MG996R hobby servos (teaches linkage kinematics instead of servo-bus protocol): https://www.thingiverse.com/thing:1454048
- $122: single SO-101 follower arm, self-printed parts (lose teleoperation, keep the full software path)
- $199.99: Hiwonder xArm 1S — cheapest arm with intelligent bus servos that report position/voltage: https://www.hiwonder.com/products/xarm-1s

---

## Month 4 — ROS 2 / SLAM hardware (optional — sim covers all of this at $0)

| Tier | Cost | What |
|---|---|---|
| $0 | — | Gazebo with a simulated lidar — do the entire SLAM/Nav2 curriculum here first |
| DIY | $250–450 | RPLIDAR C1 ($69) + Raspberry Pi 4/5 + diff-drive base w/ encoders + motor driver + battery |
| Ready platform | $300–535 | Hiwonder MentorPi M1 (from $299.99, ROS 2 Humble, Pi 5, lidar + depth camera): https://www.hiwonder.com/products/mentorpi-m1 — or Waveshare UGV Rover ROS 2 kit ($534.99, Pi host + ESP32 real-time controller): https://www.waveshare.com/ugv-rover-ros2-kit.htm |

---

## Months 5–6 — No new hardware required

Month 5 (control theory, kinematics, perception, MoveIt 2) and Month 6
(robot learning) reuse the SO-101 arm from Month 3 and run simulation
(MuJoCo Playground, Isaac Lab) that needs no purchase — Isaac Lab needs
RTX-class GPU hardware only if you want it, and Colab covers the RL
practice tasks for free.

---

## Running total (quality-tier path, roughly)

| Month | Approx. spend |
|---|---|
| 1 | $60–160 (tier 1–2) |
| 2 | ~$105 (line follower) + ~$134 (balancer) ≈ $240 |
| 3 | $199–800 (printer, if buying) + ~$230 (SO-101 pair) |
| 4 | $0 (sim) or $250–535 (real SLAM platform) |
| 5–6 | $0 (reuses existing hardware) |

The honest range end-to-end: **as low as ~$400** if you use Fab Lab/library
printing and simulation-only for Months 4–6, up to **~$1,800+** if you buy
a printer and a dedicated SLAM robot platform.
