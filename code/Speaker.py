import pigpio
import time

class Speaker:
    def __init__(self, pwm):
        self.pwm = pwm
        self.pi = pigpio.pi()
        self.pi.set_mode(pwm, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(pwm, 1000000)
        
    def play_alarm(self):
        for _ in range(5):
            self.pi.set_PWM_dutycycle(self.pwm, 1 * 255)
            time.sleep(0.25)
            self.pi.set_PWM_dutycycle(self.pwm, 0 * 255)
            time.sleep(0.25)

if __name__ == "__main__":
    speaker = Speaker(23)
    speaker.play_alarm()



