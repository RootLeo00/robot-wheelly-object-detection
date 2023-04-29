from gpiozero import Servo
from time import sleep

servo = Servo(16)

print("Start in the middle")
servo.mid()
print(servo.value)
print(servo)
sleep(2)
print("Go to min")
servo.min()
print(servo.value)
sleep(2)
print("Go to max")
servo.max()
print(servo.value)
sleep(2)
print("And back to middle")
servo.mid()
sleep(2)
servo.value = None;
