#!/usr/bin/python

import subprocess
from time import sleep

print(" 1 - setup device driver")
print(" 2 - remove device driver")
option=input("Select an option: ")

if (option == 1):
    subprocess.call("sudo insmod themaus.ko", shell=True)
    subprocess.call("sudo insmod themaus2.ko", shell=True)
    subprocess.call("sudo insmod themaus4.ko", shell=True)
    subprocess.call("sudo insmod themaus3.ko", shell=True)
    subprocess.call("sudo mknod -m 666 /dev/maus c 240 0", shell=True)
    subprocess.call("sudo mknod -m 666 /dev/mous c 239 0", shell=True)
    subprocess.call("sudo mknod -m 666 /dev/mauss c 238 0", shell=True)
    subprocess.call("sudo mknod -m 666 /dev/mouss c 237 0", shell=True)
    subprocess.call("echo 'Setup finished'", shell=True)

elif (option == 2):
    subprocess.call("sudo rmmod themaus", shell=True)
    subprocess.call("sudo rmmod themaus2", shell=True)
    subprocess.call("sudo rmmod themaus3", shell=True)
    subprocess.call("sudo rmmod themaus4", shell=True)
    subprocess.call("sudo rm /dev/maus", shell=True)
    subprocess.call("sudo rm /dev/mous", shell=True)
    subprocess.call("sudo rm /dev/mauss", shell=True)
    subprocess.call("sudo rm /dev/mouss", shell=True)
    subprocess.call("echo 'module removed from kernel space'", shell=True)

else:
    print("You have selected an invalid option")
