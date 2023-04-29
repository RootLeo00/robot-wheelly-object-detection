import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(27, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

def forward(sec):
 init()
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 #gpio.cleanup()

def backward(sec):
 init()
 gpio.output(17, False)
 gpio.output(27, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 #gpio.cleanup()

def forwardleft(sec):
 init()
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 #gpio.cleanup()


def backwardleft(sec):
 init()
 gpio.output(17, False)
 gpio.output(27, True)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 #gpio.cleanup()


def forwardleft(sec):
 init()
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 #gpio.cleanup()


def forwardright(sec):
 init()
 gpio.output(17, False)
 gpio.output(27, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 #gpio.cleanup()


def backwardright(sec):
 init()
 gpio.output(17, False)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 #gpio.cleanup()


def stop():
 init()
 gpio.output(17, False)
 gpio.output(27, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(1)
 #gpio.cleanup()

##TESTING   
# print( "forward")
# forward(1)
# print ("backward")
# backward(1)
# print("forward left")
# forwardleft(1)
# print("backward left")
# backwardleft(1)
# print("forward right")
# forwardright(1)
# print("backward right")
# backwardright(1)
