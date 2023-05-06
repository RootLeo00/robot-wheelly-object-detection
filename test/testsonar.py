import time
import RPi.GPIO as gpio
import sys
sys.path.append('../')
from sonar import Sonar

if __name__ == '__main__':
    try:
       while True:
        sonar = Sonar()
        print ("Measured Distance = %.1f cm" % sonar.distance())
        time.sleep(1)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
       print("Measurement stopped by User")
       gpio.cleanup()
       sys.exit()


