# ECE 4180 Final Project - Dummy Bot
<p align="center">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/500d28cca542fc554b31a36479b3f6cfc9b4c036/IMG_5728.jpg" width="400">
</p>

## Brief Project Description ##



In this project, our team created a bluetooth-controlled robot. The robot can be controlled on a Flask website that is created when running the code. The robot will be controlled via a Bluetooth GUI interface with a live-camera feed streamed to a laptop where the user can control the movement of the robot. In addition, there is an autonomous, line-following functionality. After the robot has navigated to a line, on the push of a button on the webpage, the robot will autonomously follow the line using 2 IR sensors. LED's were used to alert when a line has been succesfully detected. A crash detection system was also implemented using sonors when the robot gets too close to an object, a sound on the speaker will be played to alert the user.


## Getting Started ##

### Parts List ###
1. [Raspberry Pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
2. [Shadow Chassis](https://www.sparkfun.com/products/13301)
3. [Motor](https://www.sparkfun.com/products/13302) (2)
4. [65 mm Wheel](https://www.sparkfun.com/products/13259) (2)
5. [Breadboard](https://www.sparkfun.com/products/12002)
6. [Obstacle Avoidance Sensor module](https://www.amazon.com/OSOYOO-Infrared-Obstacle-Avoidance-Arduino/dp/B01I57HIJ0)(2)
7. [Speaker](https://www.sparkfun.com/products/11089)
8. [Jumper Wires - Male to Male, Male to Female, and Female to Female](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY/ref=sr_1_3?crid=OV5MBZZ8V4T8&keywords=male+to+male+jumper+wires&qid=1639343284&s=electronics&sprefix=male+to+male+jump%2Celectronics%2C146&sr=1-3) (120 Pack)
9. [Resistor 1K Ohm](https://www.sparkfun.com/products/14492)
10. [Resistor 220 Ohm](https://www.sparkfun.com/products/17994)
11. [Dual H-Bridge](https://www.sparkfun.com/products/14450)
12. [Ultrasonic Distance Sensor](https://www.sparkfun.com/products/15569)
13. [Raspberry Pi Camera](https://www.raspberrypi.com/products/camera-module-v2/)
14. [200 mA Transistor](https://www.sparkfun.com/products/521)
15. [Green Diffused LED](https://www.sparkfun.com/products/10633)
16. [Electrical Tape](https://www.amazon.com/Scotch-Electrical-Tape-4-Inch-66-Foot/dp/B001ULCB1O)
17. [External Power Bank](https://www.amazon.com/Alongza-Portable-Charger-10000mAh-External/dp/B082X53VDL/ref=sr_1_34?keywords=small+external+power+supply&qid=1639343777&s=electronics&sr=1-34)
18. [Battery Cover](https://www.sparkfun.com/products/12083)
19. [DC Barrel Power Jack](https://www.sparkfun.com/products/119)

### Hardware Setup (Wiring) ###

#### Obstacle Avoidance Sensor module ####
