import time

from flask import Flask, render_template, request, redirect, url_for, make_response

import RPi.GPIO as GPIO
from gpiozero import LineSensor
from PWMMotor import PWMMotor
from Robot import Robot

from threading import Thread, Event
from Sonar import Sonar, SonarThread
from line_following import LineThread


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    change_pin = int(changepin)
    if change_pin == 1:
        print("Forward")
        robot.forward()
    elif change_pin == 2:
        print("Left")
        robot.left()
    elif change_pin == 3:
        print("Right")
        robot.right()
    elif change_pin == 4:
        print("Reverse")
        robot.backward()
    elif change_pin == 5:
        print("Stop")
        robot.stop()
    elif change_pin == 6:
        print("Start line following")
        GPIO.output(25, True)
        robot.set_speed(0.45)
        line_event.set()
        sonar_event.clear()
    elif change_pin == 7:
        print("Stop line following")
        GPIO.output(25, False)
        robot.stop()
        robot.set_speed(0.5)
        line_event.clear()
        sonar_event.set()
        
    return make_response(redirect(url_for('index')))

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    left_sensor = LineSensor(17)
    right_sensor = LineSensor(27)
    left_motor = PWMMotor(8, 7, 12)
    right_motor = PWMMotor(9, 10, 13)
    robot = Robot(left_motor, right_motor, left_sensor, right_sensor, speed=0.5)
    line_event = Event()
    line_thread = LineThread(line_event, robot)
    sonar = Sonar(23, 24)
    sonar_event = Event()
    sonar_thread = SonarThread(sonar_event, sonar, left_motor, right_motor)
    sonar_thread.daemon = True
    line_event.clear()
    sonar_event.set()
    line_thread.daemon = True
    line_thread.start()
    sonar_thread.start()
    app.run(host='0.0.0.0', port=8000)
        
        

