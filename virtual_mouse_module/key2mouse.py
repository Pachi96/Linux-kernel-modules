#!/usr/bin/python

from time import sleep
import sys, tty, termios
import subprocess

c1=0
c2=0
c3=0
c4=0

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:

    char=getch()
    if (char == 'A'):
	subprocess.call("cat /dev/maus", shell=True)
	sleep(0.01)
	if (c1 == 0):
		print('                    ^')
		print('                   / \ ')
		print('                  /   \ ')
		print('                 /_   _\ ')
		print('                   | |')
		print('                   | |')
		print('                   |_|')
	if c2>0 or c3>0 or c4>0:
	    c2=0
	    c3=0
	    c4=0
	c1+=1

    elif(char == 'B'):
	subprocess.call("echo hi > /dev/maus", shell=True)
	sleep(0.01)
	if (c2 == 0):
	    print('                    _')
	    print('                   | |')
	    print('                   | |')
	    print('                 __| |__')
	    print('                 \     /')
	    print('                  \   /')
	    print('                   \ /')
	    print('                    v')
	if c1>0 or c3>0 or c4>0:
	    c1=0
	    c3=0
	    c4=0
	c2+=1

    elif(char == 'C'):
	subprocess.call("cat /dev/mous", shell=True)
        sleep(0.01)	
	if (c3 == 0):
	    print('                        |\ ')
	    print('                   _____| \ ')
	    print('                  |        \ ')
	    print('                  |_____   /')
	    print('                        | /')
	    print('                        |/')

	if c1>0 or c2>0 or c4>0:
	    c1=0
	    c2=0
	    c4=0
	c3+=1

    elif(char == 'D'):
	subprocess.call("echo hi > /dev/mous", shell=True)
	sleep(0.01)
	if (c4 == 0):
	    print('                    /|')
	    print('                   / |_____')
	    print('                  /        |')
	    print('                  \   _____|')
	    print('                   \ |')
	    print('                    \|')
	    
	if c1 >0 or c3 >0 or c2>0:
	    c1=0
            c3=0
            c2=0
	c4+=1
	
    elif(char == 'c'):
        sys.exit(0)
