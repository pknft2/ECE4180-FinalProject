# ECE 4180 Final Project - Dummy Bot

**Team Members:** Devarsi Rawal, Christopher Burgett, Dylan Kynoch, Thomas Petrick 


<p align="center">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/500d28cca542fc554b31a36479b3f6cfc9b4c036/IMG_5728.jpg" width="400">
</p>

## Demo Video ##
[Click here to watch the demo video](https://drive.google.com/file/d/1T7-IjlprSwlbDVLUfga_Zg4BycERbjxR/preview)


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

#### Obstacle Avoidance Sensor modules ####

<p align="left">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/cd7bae4ffe6b8fe3ce1d59c48750e090fb257a88/images/circuit.png" width="400">
</p>

#### Speaker ####

<p align="left">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/0fe1c11d0b63ebe17f9462220c63f7d08fec130f/images/speaker.png" width="400">
</p>

#### Sonar ####

<p align="left">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/a6d8070e16e2f38da2f6ff92a71209e0e0f5395e/images/sonar.png" width="400">
</p>

#### Motors ####

<p align="left">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/58a6084d8c30eaf722c3631d64497e00d288d69c/images/motorCircuit.png" width="400">
</p>

#### Green LED ####

<p align="left">
<img src="https://github.com/tpetrick3/ECE4180-FinalProject/blob/58a6084d8c30eaf722c3631d64497e00d288d69c/images/greenLED.png" width="400">
</p>

### Software Setup ###

#### Raspberry Pi ####

To install Raspberry Pi OS on your Raspberry Pi 3B, follow the official instructions [here](https://www.raspberrypi.com/software/). Make sure Python 3.9.7 is installed.

#### Camera Setup ####

*If on Pi OS 11 (Bullseye), in order for the camera to work correctly you may need to enable graphic acceleration by running `$ sudo raspi-config` > Advanced Options > Glamor > Enable*

On the Raspberry Pi, to start the video stream, run:
```
$ libcamera-vid -t 0 --inline --listen -o tcp://0.0.0.0:8081 -n
```

On your client (if Ubuntu), to listen to the video stream, run:
```
$ ffplay tcp://<your-raspberrypi-ip>:8081 -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop
```
Alternatively, you can also access the stream via VLC using:
```
vlc tcp/h264://<your-raspberrypi-ip>:8081
```

#### Server Setup

First, clone this GitHub repository and navigate to the `code` folder using:
```
$ git clone https://github.com/tpetrick3/ECE4180-FinalProject.git
$ cd ECE4180-FinalProject/code/
```

Then, run the pigpio daemon using:
```
$ sudo pigpiod
```

Finally, to start the server, run:
```
$ python server.py
```

On your client device, navigate to \<your-raspberrypi-ip\>:8000 to view the control panel.
