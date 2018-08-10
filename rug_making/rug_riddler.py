#!/usr/bin/env python

import numpy
import time
import sys
import math

def rug_maker(colors):
	rug = list()

	# Create the rug
	for i in range(0,100):
		row = list()

		for j in range(0,100):
			row.append(int(numpy.random.randint(0,colors)))

		rug.append(row)

	# print("New rug made!")
	# print(rug)

	for i in range(0,97):
		for j in range(0,97):
			# print("Checking next 4x4")
			keep = False
			color_to_match = rug[i][j]
			for k in range(0,4):
				for l in range(0,4):
					if color_to_match != rug[i+k][j+l]: 
						# print("4x4 not homogenus!")
						keep = True
						break
			if not keep:
				# print("RUG NO GOOD")
				return False
	return True

if __name__=='__main__':
	start_time = time.time()
	colors = int(raw_input("How many colors do you want to use to make the rugs? "))
	trials = int(raw_input("How many rugs do you want to make (rejections included)? "))
	rejections = 0

	print("...")
	sys.stdout.write("\n\n\n\n")

	for t in range(0,trials):
		keep = rug_maker(colors)

		if not keep:
			rejections += 1

		run_time = time.time() - start_time 

		sys.stdout.write("\033[F\033[F\033[F\033[F")
		sys.stdout.write("Rugs made: " + str(t + 1))
		sys.stdout.write("\nRugs rejected: " + str(rejections))
		sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
		sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
		sys.stdout.write("\n...")
		sys.stdout.flush()
	
	print("\nSampled Probability of rug rejection: " + str(rejections/float(trials)))