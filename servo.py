import time
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

#set GPIO Pins
GPIO_PILOT = 16

 
class Servo():

    #place servo in left position
    def rotate_to_left(self):
        self.servo.max()
        time.sleep(0.5)
        
    #place servo in right position
    def rotate_to_right(self):
        self.servo.min()
        time.sleep(0.5)
        
    #place servo in middle position
    def rotate_to_middle(self):
        self.servo.mid()
        time.sleep(0.5)

    def is_rotated_left(self):
        return self.servo.value == 1.0

    def is_rotated_right(self):
        return self.servo.value == -1.0
    
    def is_rotated_middle(self):
        return self.servo.value == 0.0 or self.servo.value==-0.0
    
    def __init__(self, gpio_number):
        # initialize servo
        factory = PiGPIOFactory()
        self.servo = Servo(pin=gpio_number, pin_factory=factory)
        self.servo.mid()
