# Import libraries
import RPi.GPIO as GPIO
import time

#set GPIO Pins
GPIO_PILOT = 16
duty=0
#GPIO_POW = 26
def init():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)
    # Set gpio 16 as an output, and set servo1 as gpio 16 as PWM
    GPIO.setup(GPIO_PILOT,GPIO.OUT)
    #segnale PWM (Pulse Width Modulation) con frequenza di 50Hz
    servo1 = GPIO.PWM(GPIO_PILOT,50) # Note: 50 = 50Hz pulse



#rotate left 90 degrees
def rotateLeft_90(self):
    init()
    duty = 5
    self.ChangeDutyCycle(duty)
    time.isleep(0.5)
    self.stop()
    GPIO.cleanup()
    
#rotate left 90 degrees
def rotateRight_90(self):
    init()
    duty = 10
    self.ChangeDutyCycle(duty)
    time.sleep(0.5)
    self.stop()
    GPIO.cleanup()
    
#Posizione Neutra:
def rotateNeutral(self):
    init()
    duty = 7.5
    self.ChangeDutyCycle(duty)
    time.sleep(0.5)
    self.stop()
    GPIO.cleanup()
    
def crazyRotation(self):
    init()
    i=0
    self.start(2.5) # Initialization
    try:
      while i<100:
        self.ChangeDutyCycle(5)
        time.sleep(0.5)
        self.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        self.ChangeDutyCycle(10)
        time.sleep(0.5)
        self.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        self.ChangeDutyCycle(10)
        time.sleep(0.5)
        self.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        self.ChangeDutyCycle(5)
        time.sleep(0.5)
        self.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        i=i+1
    except KeyboardInterrupt:
      self.stop()
      GPIO.cleanup()

def getAngle():
    return duty