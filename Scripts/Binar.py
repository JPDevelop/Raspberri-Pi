import RPi.GPIO as GPIO
import time
import sys

def binar_2(pin_num, num):
	if (num%2 == 0):
		rest = True
	else:
		rest = False
	GPIO.output(pin_num, rest)
	time.sleep(0.5)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)
GPIO.output(13, True)
GPIO.output(15, True)
num = input('Enter a number please: ')
if (num <= 15 and  type(num) is int):
	binar_2(7, num)
	num /= 2	
	binar_2(11, num)
	num /= 2
	binar_2(13, num)
	num /= 2
	binar_2(15, num)
else:
	print("The computer can't handle this :(")
