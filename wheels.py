import RPi.GPIO as gpio
import time

class MotorWheels():
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(17, gpio.OUT)
        gpio.setup(27, gpio.OUT)
        gpio.setup(23, gpio.OUT)
        gpio.setup(24, gpio.OUT)

    def forward(self, sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, True) 
        gpio.output(24, False)
        time.sleep(sec)

    def backward(self, sec):
        gpio.output(17, False)
        gpio.output(27, True)
        gpio.output(23, False) 
        gpio.output(24, True)
        time.sleep(sec)

    def forwardleft(self, sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def backwardleft(self, sec):
        gpio.output(17, False)
        gpio.output(27, True)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def forwardleft(self, sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def forwardright(self, sec):
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, True) 
        gpio.output(24, False)
        time.sleep(sec)


    def backwardright(self, sec):
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, True)
        time.sleep(sec)


    def stop(self):
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(0.5)
