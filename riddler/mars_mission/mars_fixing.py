#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/in-space-no-one-can-hear-your-3d-printer-die/
"""

import numpy
import time
import sys
import math

# Mission simulator function
# Inputs are the probabilities of each printer failing on a given day: p1, p2, p3 and the mission length in days
def mission_simulator(p1, p2, p3, mission_length):

	# List of printer probabilities
	p_fail = [p1, p2, p3]

	# Day 1 printer state
	failed = [numpy.random.binomial(1,p) for p in p_fail]

	# Simulating each day on the mission
	for day_no in range(1, mission_length+1):

		# If all 3 printers have failed you die
		if failed.count(1) == 3:
			return [False, day_no]

		# If two printers have failed then you are stuck with only 1 to keep you alive.  Re-roll that one only in that index
		if failed.count(1) == 2:
			failed[failed.index(0)] = numpy.random.binomial(1, p_fail[failed.index(0)])

		# If one printer failed then re-roll the other two.  Do this by finding the failed printer and then re-rolling the other two indexes
		if failed.count(1) == 1:
			failed[failed.index(1) - 1] = numpy.random.binomial(1, p_fail[failed.index(1) - 1])
			failed[failed.index(1) - 2] = numpy.random.binomial(1, p_fail[failed.index(1) - 2])

			# If the two re-rolls succeed then we can fix the 3rd printer
			if failed.count(1) == 1:
				failed = [0, 0, 0]

		# If all 3 printers are operational then re-roll them all
		if failed.count(1) == 0:
			failed = [numpy.random.binomial(1,p) for p in p_fail]
	
	# If you make it to the end of the mission then you live!		
	return [True, day_no]



if __name__=='__main__':
	start_time = time.time()

	# User input values for printer probabilities, mission length, and number of missions to simulate
	p1 = float(raw_input("What's the probability of printer 1 failing in a given day? "))
	p2 = float(raw_input("What's the probability of printer 2 failing in a given day? "))
	p3 = float(raw_input("What's the probability of printer 3 failing in a given day? "))
	days = int(raw_input("How many days is the mission to Mars? "))
	trials = int(raw_input("How many missions do you want to simulate? "))

	print("...")
	sys.stdout.write("\n\n\n\n\n")

	# Initial values for missions failed, missions succeeded, total days survived in all missions, and the longest mission before failure
	deaths = 0
	mission_success = 0
	cum_days_survived = 0
	max_days_survived = 0

	# Simulating missions
	for t in range(0,trials):
		# Call mission simulator with parameters
		status = mission_simulator(p1, p2, p3, days)

		# Gathering return data of number of days survived for specific mission
		cum_days_survived += status[1]
		max_days_survived = max( [status[1], max_days_survived])

		# Gathering whether the specific mission succeeded or not
		if status[0]:
			mission_success += 1
		else:
			deaths += 1

		run_time = time.time() - start_time 

		# Output data
		sys.stdout.write("\033[F\033[F\033[F\033[F\033[F\033[F")
		sys.stdout.write("Missions simulated: " + str(t + 1))
		sys.stdout.write("\nTimes died: " + str(deaths))
		sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
		sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
		sys.stdout.write("\nAverage days survived: " + str( cum_days_survived / (t+1)) + " days     ")
		sys.stdout.write("\nLongest mission: " + str(max_days_survived) + " days     ")
		sys.stdout.write("\n...")
		sys.stdout.flush()

	# Final output of empirical chance of survival
	print("\nSampled probability of mission success: " + str(1 - deaths/float(trials)))