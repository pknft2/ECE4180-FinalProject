import pigpio
import time

class Speaker:
    def __init__(self, pwm):
        self.pwm = pwm
        self.pi = pigpio.pi()
        
        
    def play_alarm(self):
        for i in range(4):
            self.pi.hardware_PWM(self.pwm, 969, int(i*0.1*1000000))
            time.sleep(0.5)
            self.pi.hardware_PWM(self.pwm, 800, int(i*0.1*1000000))
            time.sleep(0.5)
        self.pi.hardware_PWM(self.pwm, 969, 0)
            
if __name__ == "__main__":
    speaker = Speaker(18)
    speaker.play_alarm()



