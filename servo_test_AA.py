# Import libraries
import RPi.GPIO as GPIO
import time
import servo

#set GPIO Pins
GPIO_PILOT = 16
#GPIO_POW = 26

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set gpio 16 as an output, and set servo1 as gpio 16 as PWM
GPIO.setup(GPIO_PILOT,GPIO.OUT)

#segnale PWM (Pulse Width Modulation) con frequenza di 50Hz
servo1 = GPIO.PWM(GPIO_PILOT,50) # Note: 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty
duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    # where 0.0 <= dc <= 100.0
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(2)

#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
#GPIO.output(GPIO_POW, False)
#Clean things up at the endj
servo1.stop()
GPIO.cleanup()
print ("Goodbye")

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PILOT, GPIO.OUT)

pwm=GPIO.PWM(GPIO_PILOT, 50)
pwm.start(0)

## edit these duty cycle % values ##
left = 2.5
neutral = 7.5
right = 12

print("begin test2")

print("duty cycle", left,"% at left -90 deg")
pwm.ChangeDutyCycle(2.5)
sleep(1)

print("duty cycle", neutral,"% at 0 deg")
pwm.ChangeDutyCycle(neutral)
sleep(1)

print("duty cycle",right, "% at right +90 deg")
pwm.ChangeDutyCycle(right)
sleep(1)

print("end of test")

pwm.stop()
GPIO.cleanup()