import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
while True:
	char = raw_input('Enter a command for help type \'help\': ')
	if char == 'sos':
		while True:
			GPIO.output(7,False)
			time.sleep(1)
			GPIO.output(7,True)
			time.sleep(0.5)
			GPIO.output(7,False)
			time.sleep(0.3)
			GPIO.output(7,True)
			time.sleep(0.5)
			GPIO.output(7,False)
			time.sleep(1)
			GPIO.output(7,True)
			time.sleep(2)
	if char == 'help':
		print('sos: morse sos code\nstop: turn off the lamp\nother: turn on the lamp')	
	if char == 'stop':
		GPIO.output(7,True)
	else:
		GPIO.output(7,False)
