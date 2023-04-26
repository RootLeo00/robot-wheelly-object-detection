# Import libraries
import RPi.GPIO as GPIO
import time

#set GPIO Pins
GPIO_PILOT = 16
duty=-1
 
class servo2():

    #   rotate left 90 degrees
    def rotateLeft_90(self):
        duty = 5
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.pwm.stop()
        GPIO.cleanup()
        
    #rotate left 90 degrees
    def rotateRight_90(self):
        duty = 10
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.stop()
        GPIO.cleanup()
        
    #Posizione Neutra:
    def rotateNeutral(self):
        #nit()
        duty = 7.5
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.stop()
        GPIO.cleanup()
        
    def getAngle(self):
        #init()
        angle=self.value*90
        print("angle: "+ angle)
        return angle

    def rotate(self, angle):
        duty = float(angle) / 9.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)
    


    
    def __init__(self):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        # Set gpio 16 as an output, and set servo1 as gpio 16 as PWM
        GPIO.setup(GPIO_PILOT,GPIO.OUT)
        #segnale PWM (Pulse Width Modulation) con frequenza di 50Hz
        self.pwm = GPIO.PWM(GPIO_PILOT,50) # Note: 50 = 50Hz pulse
        self.value=-2
        duty=-2
