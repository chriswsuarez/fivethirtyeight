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

		# Generating each row of the rug
		for j in range(0,100):
			row.append(int(numpy.random.randint(0,colors)))

		rug.append(row)

	# print("New rug made!")
	# print(rug)

	# Searching each possible 4x4 block.
	# 97 must be used because there are only 97x97 distinct 4x4 blocks in a 100x100 grid
	for i in range(0,97):
		for j in range(0,97):
			# print("Checking next 4x4")
			keep = False

			# Grabbing the first color of the 4x4 and all colors must match this for rejection
			color_to_match = rug[i][j]

			# Iterating through the 4x4 block and checking each color against the first 1x1
			for k in range(0,4):
				for l in range(0,4):

					# If the color does not match the first 1x1 then we can move on to the next 4x4 immediately
					if color_to_match != rug[i+k][j+l]: 
						# print("4x4 not homogenus!")
						keep = True
						break
			
			# If keep is not true after we have gone through the entire 4x4 then we must reject the rug
			if not keep:
				# print("RUG NO GOOD")
				return False

	# If we make it all the way through without returning false then the rug is good to go
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
	
	print("\nSampled probability of rug rejection: " + str(rejections/float(trials)))