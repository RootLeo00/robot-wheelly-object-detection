from servo import Servo
import time
import RPi.GPIO as gpio
import sys

if __name__ == '__main__':
    try:
        servo=Servo(16)
        print("rotate neutral")
        servo.rotate_to_middle()
        print("servo value",servo.servo.value)
        print("Is servo rotated to the middle position?",servo.is_rotated_middle())
        time.sleep(2)
        print("rotate left")
        servo.rotate_to_left()
        print("servo value", servo.servo.value)
        print("Is servo rotated to the left position?",servo.is_rotated_left())
        time.sleep(2)
        print("rotate right")
        servo.rotate_to_right()
        print("servo value",servo.servo.value)
        print("Is servo rotated to the right position?", servo.is_rotated_right())
        time.sleep(2)
        print("rotate neutral")
        servo.rotate_to_middle()

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
       print("Servo stopped by User")
       gpio.cleanup()
       sys.exit()