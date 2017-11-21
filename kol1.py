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

class Plane:
	def __init__(self, start_angle, tilt_correction_step):
		self.angle = start_angle
		self.tilt_correction_step = tilt_correction_step
	def get_actual_angle(self):
		return self.angle
	def add_turbulence(self, turbulence):
		self.angle += turbulence
	def apply_tilt_correction(self):
		if self.angle < 0:
			self.angle += self.tilt_correction_step
		else:
			self.angle -= self.tilt_correction_step
	def change_tilt_correction_step(self, new_tilt_correction_step):
		self.tilt_correction_step = new_tilt_correction_step
	
class Turbulence:
	def __init__(self, gaussian_distribution_mean, gaussian_distribution_sigma):
		self.gaussian_distribution_mean = gaussian_distribution_mean
		self.gaussian_distribution_sigma = gaussian_distribution_sigma
	def generate_turbulance(self):
		return random.gauss(self.gaussian_distribution_mean, self.gaussian_distribution_sigma)
	def get_gaussian_distribution_mean(self):
		return self.gaussian_distribution_mean
	def change_gaussian_distribution_mean(self, new_gaussian_distribution_mean):
		self.gaussian_distribution_mean = new_gaussian_distribution_mean
	def get_gaussian_distribution_sigma(self):
		return self.gaussian_distribution_sigma
	def change_gaussian_distribution_sigma(self, new_gaussian_distribution_sigma):
		self.gaussian_distribution_sigma = new_gaussian_distribution_sigma
		
if __name__ == "__main__":

	print("--------------------------")
	print("| Starting simulation... |\n| Press 'Ctrl+C' to exit |")
	print("--------------------------\n")
	
	plane = Plane(0,2)
	turbulance = Turbulence(0.0, 1.0)

	while True:
		plane.add_turbulence(turbulance.generate_turbulance())
		print("Current angle: {:.4f}".format(plane.get_actual_angle()))
		plane.apply_tilt_correction()
		print("After angle correction: {:.4f}\n".format(plane.get_actual_angle()))
		time.sleep(1)
