from gpiozero import CompositeDevice, SourceMixin, PWMOutputDevice, DigitalOutputDevice, OutputDeviceBadValue
from collections import OrderedDict

# Run $sudo pigpiod before importing
import pigpio

class PWMMotor(SourceMixin, CompositeDevice):
    
    def __init__(self, forward, backward, pwm, *, pin_factory=None):
        devices = OrderedDict((
            ('forward_device', DigitalOutputDevice(forward, pin_factory=pin_factory)),
            ('backward_device', DigitalOutputDevice(backward, pin_factory=pin_factory))
        ))
        self.pwm = pwm
        self.pi = pigpio.pi()
        self.pi.set_mode(pwm, pigpio.OUTPUT)
        super().__init__(_order=devices.keys(), **devices)
        
    @property
    def value(self):
        return self.pi.get_PWM_dutycycle()
    
    @value.setter
    def value(self, value):
        if not 0 <= value <= 1:
            raise OutputDeviceBadValue("Motor speed must be between 0 and 1")
        self.pi.set_PWM_dutycycle(self.pwm, value * 255)
    
    def forward(self, speed=1):
        self.backward_device.off()
        self.forward_device.on()
        self.value = speed
        
    def backward(self, speed=1):
        self.forward_device.off()
        self.backward_device.on()
        self.value = speed
    
    def stop(self):
        self.forward_device.off()
        self.backward_device.off()
        self.value = 0

