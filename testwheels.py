from wheels import MotorWheels
import RPi.GPIO as gpio
import sys

if __name__ == '__main__':
    try:
        wheels=MotorWheels()
        print( "forward")
        wheels.forward(1)
        print ("backward")
        wheels.backward(1)
        print("forward left")
        wheels.forwardleft(1)
        print("backward left")
        wheels.backwardleft(1)
        print("forward right")
        wheels.forwardright(1)
        print("backward right")
        wheels.backwardright(1)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
       print("Wheels stopped by User")
       gpio.cleanup()
       sys.exit()


