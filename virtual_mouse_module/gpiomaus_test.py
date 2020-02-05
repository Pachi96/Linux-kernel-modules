#!/usr/bin/python

from time import sleep
import sys, tty, termios
import subprocess

def repeat_motion(times, option, dev_name):
    if option == 1: #cat
	for i in range (times):
	    subprocess.call("cat /dev/"+dev_name, shell=True)
	    sleep(0.01)
    elif option == 2: #echo
	for i in range (times):
	    subprocess.call("echo hi > /dev/"+dev_name, shell=True)
            sleep(0.01)

try:
    while True:

	print("                            +-----------------------+")
	print("                            | 8 - up                |")
	print("                            | 9 - up and right      |")
	print("                            | 7 - up and left       |")
	print("                            | 2 - down              |")
	print("                            | 3 - down and right    |")
	print("                            | 1 - down and left     |")
	print("                            | 4 - left              |")
	print("                            | 6 - right             |")
	print("                            +-----------------------+")
	option=input("                         Select an option from 1 to 8: ")
	times=input ("                         How many times?: ")

	if (option == 8):
	    repeat_motion(times,1,"maus")

	elif (option == 9):
	    repeat_motion(times,1,"mauss")

	elif (option == 7):
	    repeat_motion(times,2,"mauss")

	elif(option == 2):
	    repeat_motion(times,2,"maus")

	elif (option == 3):
	    repeat_motion(times,1,"mouss")

	elif (option == 1):
	    repeat_motion(times,2,"mouss")
	    
	elif(option == 4):
	    repeat_motion(times,2,"mous")

	elif(option == 6):
	    repeat_motion(times,1,"mous")

        subprocess.call("clear -all", shell=True)

except KeyboardInterrupt:
    subprocess.call("clear -all", shell=True)
    sys.exit()
