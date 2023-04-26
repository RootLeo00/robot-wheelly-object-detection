from servo_class import Servo
import time
import RPi.GPIO as GPIO

servo=Servo(0)
servo.rotateNeutral()
print(servo.duty)
time.sleep(2)
print("rotate left")
servo.rotateLeft_90()
time.sleep(2)
print(servo.duty)
print("rotate right")
servo.rotateRight_90()
time.sleep(2)
servo.pwm.stop()
GPIO.cleanup()

