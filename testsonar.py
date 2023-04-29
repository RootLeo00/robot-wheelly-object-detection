import time
from sonar import Sonar
import RPi.GPIO as gpio
import sys

if __name__ == '__main__':
    try:
       while True:
        sonar = Sonar()
        print ("Measured Distance = %.1f cm" % sonar.distance)
        time.sleep(1)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
       print("Measurement stopped by User")
       gpio.cleanup()
       sys.exit()

