import RPi.GPIO as GPIO
import time

def Long():
	GPIO.output(7, False)
	time.sleep(0.8)
	GPIO.output(7, True)
	time.sleep(0.3)
def short():
	GPIO.output(7, False)
	time.sleep(0.2)
	GPIO.output(7, True)
	time.sleep(0.3)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7, True)
Wor = raw_input('Enter a wor: ')
position = 0
while (position != len(Wor)):
	print(Wor[position])
	time.sleep(2)
	if (Wor[position]) == 'a':
		short()
		Long()
	elif (Wor[position]) == 'b':
		Long()
		short()
		short()
		short()
	elif (Wor[position]) == 'c':
		Long()
		short()
		Long()
		short()
	elif (Wor[position]) == 'd':
		Long()
		short()
		short()
	elif (Wor[position]) == 'e':
		short()
	elif (Wor[position]) == 'f':
		short()
		short()
		Long()
		short()
	elif (Wor[position]) == 'g':
		Long()
		Long()
		short()
	elif (Wor[position]) == 'h':
		short()
		short()
		short()
		short()
	elif (Wor[position]) == 'i':
		short()
		short()
	elif (Wor[position]) == 'j':
		short()
		Long()
		Long()
		Long()
	elif (Wor[position]) == 'k':
		Long()
		short()
		Long()
	elif (Wor[position]) == 'l':
		short()
		Long()
		short()
		short()
	elif (Wor[position]) == 'm':
		Long()
		Long()
	elif (Wor[position]) == 'n':
		Long()
		short()
	elif (Wor[position]) == 'o':
		Long()
		Long()
		Long()
	elif (Wor[position]) == 'p':
		short()
		Long()
		Long()
		short()
	elif (Wor[position]) == 'q':
		Long()
		Long()
		short()
		Long()
	elif (Wor[position]) == 'r':
		short()
		Long()
		short()
	elif (Wor[position]) == 's':
		short()
		short()
		short()
	elif (Wor[position]) == 't':
		Long()
	elif (Wor[position]) == 'u':
		short()
		short()
		Long()
	elif (Wor[position]) == 'v':
		short()
		short()
		short()
		Long()
	elif (Wor[position]) == 'w':
		short()
		Long()
		Long()
	elif (Wor[position]) == 'x':
		Long()
		short()
		short()
		Long()
	elif (Wor[position]) == 'y':
		Long()
		short()
		Long()
		Long()
	elif (Wor[position]) == 'z':
		Long()
		Long()
		short()
		short()
	elif(Wor[position]) == ' ':
		GPIO.output(7, False)
		time.sleep(4)
		GPIO.output(7, True)
		time.sleep(0.3)
	position += 1
