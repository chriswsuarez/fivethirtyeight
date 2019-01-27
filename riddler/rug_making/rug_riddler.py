#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/where-on-earth-is-the-riddler/
"""

import numpy
import time
import sys
import math

# Rug simulation function
def rug_maker(colors):
	rug = list()

	# Create the rug row by row
	for i in range(0,100):
		row = list()

		# Generating each row of the rug
		for j in range(0,100):
			row.append(int(numpy.random.randint(0,colors)))

		# Stitch the rug together row by row
		rug.append(row)

	# Searching each possible 4x4 block.
	# 97 must be used because there are only 97x97 distinct 4x4 blocks in a 100x100 grid
	for i in range(0,97):
		for j in range(0,97):

			# 4x4 must be completly examined to keep
			keep = False

			# Grabbing the first color of the 4x4 and all colors must match this for rejection
			color_to_match = rug[i][j]

			# Iterating through the 4x4 block and checking each color against the first 1x1
			for k in range(0,4):
				for l in range(0,4):

					# If the color does not match the first 1x1 then we can move on to the next 4x4 immediately
					if color_to_match != rug[i+k][j+l]: 
						keep = True
						break
			
			# If keep is not true after we have gone through the entire 4x4 then we must reject the rug
			if not keep:
				return False

	# If we make it all the way through without returning false then the rug is good to go
	return True

if __name__=='__main__':
	start_time = time.time()

	# Input for our rug manufacturing plant
	colors = int(raw_input("How many colors do you want to use to make the rugs? "))
	trials = int(raw_input("How many rugs do you want to make (rejections included)? "))
	rejections = 0

	print("...")
	sys.stdout.write("\n\n\n\n")

	# Simulating our manufacturing order of rugs!
	for t in range(0,trials):
		# Make a rug
		keep = rug_maker(colors)

		# Record rejection counter
		if not keep:
			rejections += 1

		run_time = time.time() - start_time 

		# Output data
		sys.stdout.write("\033[F\033[F\033[F\033[F")
		sys.stdout.write("Rugs made: " + str(t + 1))
		sys.stdout.write("\nRugs rejected: " + str(rejections))
		sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
		sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
		sys.stdout.write("\n...")
		sys.stdout.flush()
	
	# Output final probability of rug rejection
	print("\nSampled probability of rug rejection: " + str(rejections/float(trials)))