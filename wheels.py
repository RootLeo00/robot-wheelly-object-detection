import RPi.GPIO as gpio
import time

class MotorWheels():
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(17, gpio.OUT)
        gpio.setup(27, gpio.OUT)
        gpio.setup(23, gpio.OUT)
        gpio.setup(24, gpio.OUT)

    def forward(sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, True) 
        gpio.output(24, False)
        time.sleep(sec)

    def backward(sec):
        gpio.output(17, False)
        gpio.output(27, True)
        gpio.output(23, False) 
        gpio.output(24, True)
        time.sleep(sec)

    def forwardleft(sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def backwardleft(sec):
        gpio.output(17, False)
        gpio.output(27, True)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def forwardleft(sec):
        gpio.output(17, True)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(sec)


    def forwardright(sec):
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, True) 
        gpio.output(24, False)
        time.sleep(sec)


    def backwardright(sec):
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, True)
        time.sleep(sec)


    def stop():
        gpio.output(17, False)
        gpio.output(27, False)
        gpio.output(23, False) 
        gpio.output(24, False)
        time.sleep(0.5)