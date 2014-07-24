import RPi.GPIO as GPIO
import time
import sys
import random
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
while True:
	GPIO.output(7, random.choice([True, False]))
	GPIO.output(11, random.choice([True, False]))
	GPIO.output(13, random.choice([True, False]))
	time.sleep(random.uniform(0.001, 0.1))
