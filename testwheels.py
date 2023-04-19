import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

print('start setup gpio')

GPIO.setup(17,GPIO.OUT) #17 purple
GPIO.setup(27,GPIO.OUT) #27 white
                        #30 grnd
GPIO.setup(23,GPIO.OUT) #23 brown
GPIO.setup(24,GPIO.OUT) #34 orange

print('end setup')

print('left forward')
GPIO.output(17,GPIO.HIGH)
time.sleep(3)
GPIO.output(17,GPIO.LOW)

print('left backward')
GPIO.output(27,GPIO.HIGH)
time.sleep(3)
GPIO.output(27,GPIO.LOW)


print('right forward')
GPIO.output(23,GPIO.HIGH)
time.sleep(3)
GPIO.output(23,GPIO.LOW)

print('right backward')
GPIO.output(24,GPIO.HIGH)
time.sleep(3)
GPIO.output(24,GPIO.LOW)

print('all forward')
GPIO.output(17,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(3)
GPIO.output(17,GPIO.LOW)
GPIO.output(23,GPIO.LOW)


print('all backward')
GPIO.output(27,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
time.sleep(3)
GPIO.output(27,GPIO.LOW)
GPIO.output(24,GPIO.LOW)



GPIO.cleanup()
print("the end")
exit()
