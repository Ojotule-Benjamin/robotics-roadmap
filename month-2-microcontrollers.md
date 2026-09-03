# Month 2 — Microcontrollers, Motors, Sensors, First Moving Robots

Goal: a robot that moves, senses its environment, and corrects itself.

## Week 1 — Arduino

- [ ] Day 1 — [Paul McWhorter Arduino Lessons](https://toptechboy.com/arduino-lessons/): setup + first blink/digitalWrite examples
- [ ] Day 2 — digitalRead + a button; add debouncing
- [ ] Day 3 — analogRead + analogWrite: understand what PWM actually is ([Arduino docs](https://docs.arduino.cc/learn/))
- [ ] Day 4 — Interrupts: rewrite the button example to use an interrupt instead of polling
- [ ] Day 5 — Serial debugging: print sensor values, get comfortable with the serial monitor as your primary tool
- [ ] Day 6 — non-blocking timing: replace every delay() in your code so far with millis()-based timing
- [ ] Day 7 — Build the reaction-timer game (random delay → LED → button stops clock → prints ms to serial). Reference: [Arduino Built-in Examples](https://docs.arduino.cc/built-in-examples/), [Project Hub](https://projecthub.arduino.cc/) — **Week 1 checkpoint, push to GitHub**

## Week 2 — ESP32

- [ ] Day 8 — [Random Nerd Tutorials ESP32 getting-started](https://randomnerdtutorials.com/getting-started-with-esp32/): flash first sketch
- [ ] Day 9 — Order [ESP32-S3-DevKitC-1](https://www.adafruit.com/product/5312) ($15.95) + [classic ESP32 Dev Board](https://www.adafruit.com/product/3269) ($15.00) if you haven't. Meanwhile read [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html) vs [Arduino ESP32 Core docs](https://docs.espressif.com/projects/arduino-esp32/en/latest/) to understand the two layers
- [ ] Day 10 — WiFi basics: connect to your network, print IP to serial ([DroneBot Workshop ESP32 hub](https://dronebotworkshop.com/esp32-2/))
- [ ] Day 11 — I2C: wire and read one I2C sensor from its datasheet address (no tutorial-copying — find the address yourself)
- [ ] Day 12 — SPI: wire and read one SPI device
- [ ] Day 13 — Build a small async web server on the ESP32 showing live sensor readings
- [ ] Day 14 — Add buttons to that web page that drive a servo; control it from your phone on the same network — **Week 2 checkpoint, push to GitHub**

## Week 3 — Motors and drivers

- [ ] Day 15 — [DroneBot Workshop: DC motor + L298N theory](https://dronebotworkshop.com/dc-motors-l298n-h-bridge/) (learn it, but plan to not use it — obsolete, drops ~2V, runs hot)
- [ ] Day 16 — [SparkFun TB6612FNG hookup guide](https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide/all): wire the driver you'll actually use ([SparkFun breakout](https://www.sparkfun.com/sparkfun-motor-driver-dual-tb6612fng-1a.html), $14.77, or [Adafruit DRV8833](https://www.adafruit.com/product/3297), $5.95)
- [ ] Day 17 — Drive one DC motor forward/backward at 5 different PWM speeds
- [ ] Day 18 — Add an encoder ([Pololu gearmotor w/ encoder](https://www.pololu.com/product/3675), $19.95); write a function that turns the wheel exactly one revolution regardless of battery voltage (your first real closed loop)
- [ ] Day 19 — Stepper motors: wire a NEMA17 to an [A4988 driver](https://www.pololu.com/product/1182) ($8.95), run [DroneBot's stepper demos](https://dronebotworkshop.com/stepper-motors-with-arduino/)
- [ ] Day 20 — Hobby servo vs [smart bus servo](https://www.robotshop.com/products/feetech-12v-30kgcm-magnetic-encoding-servo-sts3215) vs stepper: write a one-page comparison in your own words. Optional read: [SimpleFOC docs](https://docs.simplefoc.com/) — **Week 3 checkpoint**

## Week 4 — Sensors and the physical world

- [ ] Day 21 — Wire an IMU ([MPU-6050](https://www.adafruit.com/) $12.95 or [BNO085](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085/overview) $29.50); print raw pitch/roll to serial, watch it drift when still
- [ ] Day 22 — Implement a complementary filter (angle = a*(angle+gyro*dt) + (1-a)*accelAngle); watch the drift disappear
- [ ] Day 23 — [Kalman and Bayesian Filters in Python — Roger Labbe](https://rlabbe.github.io/Kalman-and-Bayesian-Filters-in-Python/): work through the g-h and discrete Bayes chapters
- [ ] Day 24 — HC-SR04 ($3.95) or VL53L0X ($14.95): wire it, understand cone-angle limitations, log distance readings
- [ ] Day 25 — QTR reflectance array / TCRT5000 sensors: wire the line-sensor array for the line follower build. Reference: [MathWorks sensor fusion series](https://www.mathworks.com/videos/series/understanding-sensor-fusion-and-tracking.html)

## Week 5 — Build the two robots

- [ ] Day 26 — Assemble line-follower chassis + wiring (ESP32/Arduino + driver + reflectance array). Quality BOM ~$105 / budget BOM ~$38 — see SHOPPING-LIST.md
- [ ] Day 27 — Line follower: tune a P-only controller, film it oscillating/behaving badly
- [ ] Day 28 — Line follower: add the D term, film the improved run — before/after video for the portfolio
- [ ] Day 29 — Assemble self-balancer chassis + wiring (motors w/ encoders + IMU). Quality BOM ~$134 / budget BOM ~$62
- [ ] Day 30 — Self-balancer: get loop timing and the complementary filter right (this will not work until both are correct — expect frustration)
- [ ] Day 31 — Self-balancer: tune until it holds itself up for a sustained period; film it
- [ ] Day 32 — Push both robots to GitHub: wiring diagram, code, and a "what broke" writeup for each in `logs/` — **Month 2 milestone**

### Month 2 Milestone check
- [ ] Can drive a motor at controlled speed, understand PWM duty vs actual RPM
- [ ] Can read an encoder and close a position loop around it
- [ ] Can wire and read an I2C sensor from its datasheet without a tutorial
- [ ] Can fuse accel + gyro into a stable angle estimate
- [ ] Can explain P, I, D by describing what your robot did when you changed each
- [ ] Two working robots on GitHub with wiring, code, and a written account of what broke
