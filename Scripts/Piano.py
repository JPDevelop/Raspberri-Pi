import RPi.GPIO as GPIO
import time
import sys
import os

def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
def play(filename, char, char_2, pin_num):
	if char == char_2 or char == char_2.upper():
		os.system("aplay --quiet " + filename + ".wav &")
		GPIO.output(pin_num, False)
		time.sleep(0.7)
		GPIO.output(pin_num, True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)
GPIO.output(13, True)
GPIO.output(15, True)
while True:
	ch = getch()
	if ch == 'e' or ch == 'E':
		exit('')
	play('do', ch, 'a', 7)
	play('re', ch, 's', 11)
	play('mi', ch, 'd', 13)
	play('fa', ch, 'f', 15)
