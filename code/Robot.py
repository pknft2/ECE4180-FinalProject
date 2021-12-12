from PWMMotor import PWMMotor
from time import sleep

class Robot:
    
    def __init__(self, left_motor, right_motor, left_sensor, right_sensor, speed=1):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.speed = speed
        
    def set_speed(self, speed):
        self.speed = speed
        
    def forward(self):
        self.left_motor.forward(self.speed)
        self.right_motor.forward(self.speed)
    
    def left(self):
        self.left_motor.backward(self.speed)
        self.right_motor.forward(self.speed)
        
    def right(self):
        self.left_motor.forward(self.speed)
        self.right_motor.backward(self.speed)
        
    def backward(self):
        self.left_motor.backward(self.speed)
        self.right_motor.backward(self.speed)
        
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
    def left_detect(self):
        return int(self.left_sensor.value)
    
    def right_detect(self):
        return int(self.right_sensor.value)
        
    

