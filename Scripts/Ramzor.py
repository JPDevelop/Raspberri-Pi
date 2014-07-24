import RPi.GPIO as GPIO
import time
import sys
#7, orange
#11, red
#13, green
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(11, False)
time.sleep(0.7)
GPIO.output(7, False)
time.sleep(0.7)
GPIO.output(11, True)
GPIO.output(7, True)
GPIO.output(13, False)
time.sleep(0.7)
GPIO.output(13, True)
GPIO.output(7, False)
time.sleep(0.7)
GPIO.output(7, True)
GPIO.output(11, False)
time.sleep(0.7)
	
