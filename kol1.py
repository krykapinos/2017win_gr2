###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck


#!/usr/bin/env python2
import random
import time

mu = 0.0	#mean gaussian distribution
sigma = 1.0	#sigma gaussian distribution
correction = 2	#correction step of tilt
angle = 0	#tilt value

print("Starting simulation")

while True:
	angle += random.gauss(mu, sigma)		#generate turbulance
	print("Current angle: {:.4f}".format(angle))
	if angle < 0:							#applied correction
		angle += correction
	else:
		angle -= correction
	print("After angle correction: {:.4f}\n".format(angle))
	time.sleep(1)
