from time import sleep
from threading import Thread

def line_following(stop, robot):
        while True:
            if stop():
                break
            left_detect = int(robot.left_detect())
            right_detect = int(robot.right_detect())
            print(f"L: {left_detect}, R: {right_detect}")
            if left_detect == 0 and right_detect == 0:
                robot.forward()
            elif left_detect == 0 and right_detect == 1:
                robot.right()
            elif left_detect == 1 and right_detect == 0:
                robot.left()
            else:
                robot.stop()
            sleep(0.1)
            
            
class LineThread(Thread):
    
    def __init__(self, line_event, robot):
        self.robot = robot
        self.line_event = line_event
        Thread.__init__(self)
        
    def run(self):
        while True:
            self.line_event.wait()
            left_detect = int(self.robot.left_detect())
            right_detect = int(self.robot.right_detect())
            print(f"L: {left_detect}, R: {right_detect}")
            if left_detect == 0 and right_detect == 0:
                self.robot.forward()
            elif left_detect == 0 and right_detect == 1:
                self.robot.right()
            elif left_detect == 1 and right_detect == 0:
                self.robot.left()
            else:
                self.robot.stop()
            sleep(0.1)
            

