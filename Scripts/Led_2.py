import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
def Flashing (Flash, output_pin):
	while (Flash != 0):
		GPIO.output(output_pin, False)
		time.sleep(0.5)
		GPIO.output(output_pin, True)
		time.sleep(0.5)
		Flash -= 1
while True:
	GPIO.output(7, True)
	GPIO.output(11, True)
	led = raw_input('Choose one of the leds: \'red\', \'orange\' or \'both\' ')
	Flash = int(raw_input("How many Flashes? "))
	if Flash < 0:
		print('This number cannot be applied')
	if led == 'red':
		Flashing(Flash, 11)
	if led == 'orange':
		Flashing(Flash, 7)
	if led == 'both':
		while (Flash != 0):
			GPIO.output(7, False)
			GPIO.output(11, False)
			time.sleep(0.5)
			GPIO.output(7, True)
			GPIO.output(11, True)
			time.sleep(0.5)
			Flash -= 1
