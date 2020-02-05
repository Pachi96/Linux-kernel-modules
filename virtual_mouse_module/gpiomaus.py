#!/usr/bin/python

from time import sleep
import RPi.GPIO as pin
import sys, tty, termios
import subprocess

pin.setmode(pin.BCM)
pin.setwarnings(False)

up=17
down=27
left=22
right=10

pin.setup(up,pin.IN)
pin.setup(down,pin.IN)
pin.setup(left,pin.IN)
pin.setup(right,pin.IN)

try:
    while True:

	if (pin.input(up) == 1):
	    subprocess.call("cat /dev/maus", shell=True)
	    sleep(0.01)

	elif (pin.input(up) == 1 and pin.input(right) == 1):
	    #mover mouse arriba y a la derecha
	    subprocess.call("cat /dev/mauss", shell=True)
	    sleep(0.01)

	elif (pin.input(up) == 1 and pin.input(left) == 1):
	    #mover mouse arriba y a la izquierda
	    subprocess.call("echo hi > /dev/mauss", shell=True)
	    sleep(0.01)

	elif(pin.input(down) == 1):
	    subprocess.call("echo hi > /dev/maus", shell=True)
	    sleep(0.01)

	elif (pin.input(down) == 1 and pin.input(right) == 1):
	    #mover mouse abajo y a la derecha
	    subprocess.call("cat /dev/mouss", shell=True)
	    sleep(0.01)

	elif (pin.input(down) == 1 and pin.input(left) == 1):
	    #mover mouse abajo y a la izquierda
	    subprocess.call("echo hi > /dev/mouss", shell=True)
	    sleep(0.01)

	elif(pin.input(left) == 1):
	    subprocess.call("cat /dev/mous", shell=True)
	    sleep(0.01)

	elif(pin.input(right) == 1):
	    subprocess.call("echo hi > /dev/mous", shell=True)
	    sleep(0.01)

except KeyboardInterrupt:
    pin.cleanup()
    sys.exit()
