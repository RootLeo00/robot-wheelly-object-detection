import RPi.GPIO as GPIO
import time

#set GPIO Pins
GPIO_PILOT = 16

 
class Servo():

    #   rotate left 90 degrees
    def rotateLeft_90(self):
        self.duty = 2.5
        self.pwm.ChangeDutyCycle(self.duty)
        time.sleep(0.5)
        
    #rotate right 90 degrees
    def rotateRight_90(self):
        self.duty = 12
        self.pwm.ChangeDutyCycle(self.duty)
        time.sleep(0.5)
        
    #Posizione Neutra:
    def rotateNeutral(self):
        self.duty= 7.5
        self.pwm.ChangeDutyCycle(self.duty)
        time.sleep(0.5)
    
    def rotate(self, angle):
        self.duty = float(angle) / 9.0 + 2.5
        self.pwm.ChangeDutyCycle(self.duty)
    


    
    def __init__(self, duty):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        # Set gpio 16 as an output, and set servo1 as gpio 16 as PWM
        GPIO.setup(GPIO_PILOT,GPIO.OUT)
        #segnale PWM (Pulse Width Modulation) con frequenza di 50Hz
        self.pwm = GPIO.PWM(GPIO_PILOT,50) # Note: 50 = 50Hz pulse
        self.duty=duty
        self.pwm.start(0.0)
