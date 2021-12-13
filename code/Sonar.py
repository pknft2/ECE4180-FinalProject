import RPi.GPIO as GPIO
from PWMMotor import PWMMotor
from Speaker import Speaker
from threading import Thread, Event
import time

class Sonar:
    
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        
    def get_distance(self):
        # set Trigger to HIGH
        GPIO.output(self.trigger, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.0001)
        GPIO.output(self.trigger, False)
     
        start = time.time()
        stop = time.time()
     
        # save StartTime
        while GPIO.input(self.echo) == 0:
            start = time.time()
     
        # save time of arrival
        while GPIO.input(self.echo) == 1:
            stop = time.time()
     
        # time difference between start and arrival
        time_elapsed = stop - start
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (time_elapsed * 34300) / 2
     
        return distance

        
class SonarThread(Thread):
    
    def __init__(self, sonar_event, sonar, left_motor, right_motor):
        self.sonar_event = sonar_event
        self.sonar = sonar
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.speaker = Speaker(18)
        self.interrupted = False
        Thread.__init__(self)
        
    def run(self):
        while True:
            self.sonar_event.wait()
            dists = []
            for _ in range(5):
                dists.append(int(self.sonar.get_distance()))
            
            if max(set(dists), key=dists.count) < 15:
                print("Interrupted")
                self.left_motor.stop()
                self.right_motor.stop()
                self.speaker.play_alarm()
                self.left_motor.backward(0.5)
                self.right_motor.backward(0.5)
                time.sleep(1)
                self.left_motor.stop()
                self.right_motor.stop()
                
            time.sleep(0.25)
            dist = max(set(dists), key=dists.count)
            print(f"Dist: {dist:.1f}")
                
    
if __name__ == "__main__":
    left_motor = PWMMotor(8, 7, 12)
    right_motor = PWMMotor(9, 10, 13)
    sonar = Sonar(23, 24)
    speaker = Speaker(18)
    left_motor.stop()
    right_motor.stop()

    while True:
        dists = []
        for _ in range(5):
            dists.append(int(sonar.get_distance()))
            if max(set(dists), key=dists.count) < 15:
                print("Interrupted")
                speaker.play_alarm()
                time.sleep(6)
            time.sleep(0.25)
        dist = max(set(dists), key=dists.count)
        print(f"Dist: {dist:.1f}")
    

 
