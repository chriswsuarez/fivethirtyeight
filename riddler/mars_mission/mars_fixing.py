#!/usr/bin/env python

import numpy
import time
import sys
import math

def equipment_failure_simulator(p1, p2, p3, mission_length):

	p_fail = [p1, p2, p3]
	failed = [numpy.random.binomial(1,p) for p in p_fail]

	for day_no in range(0, mission_length):

		if failed.count(1) == 3:
			return [False, day_no]

		if failed.count(1) == 2:
			failed[failed.index(0)] = numpy.random.binomial(1, p_fail[failed.index(0)])

		if failed.count(1) == 1:
			failed[failed.index(1) - 1] = numpy.random.binomial(1, p_fail[failed.index(1) - 1])
			failed[failed.index(1) - 2] = numpy.random.binomial(1, p_fail[failed.index(1) - 2])

			# If the two re-rolls succeed then we can fix the 3rd printer
			if failed.count(1) == 1:
				failed = [0, 0, 0]

		if failed.count(1) == 0:
			failed = [numpy.random.binomial(1,p) for p in p_fail]
			
	return [True, day_no]


if __name__=='__main__':
	start_time = time.time()

	p1 = .1
	p2 = .075
	p3 = .05
	days = 1825
	# trials = 1

	p1 = float(raw_input("What's the probability of printer 1 failing in a given day? "))
	p2 = float(raw_input("What's the probability of printer 2 failing in a given day? "))
	p3 = float(raw_input("What's the probability of printer 3 failing in a given day? "))

	# days = int(raw_input("How many days is the mission to Mars? "))
	trials = int(raw_input("How many missions do you want to simulate? "))

	print("...")
	sys.stdout.write("\n\n\n\n\n")

	deaths = 0
	mission_success = 0
	cum_days_survived = 0
	max_days_survived = 0

	for t in range(0,trials):
		status = equipment_failure_simulator(p1, p2, p3, days)
		cum_days_survived += status[1]
		max_days_survived = max( [status[1], max_days_survived])

		if status[0]:
			mission_success += 1
		else:
			deaths += 1

		run_time = time.time() - start_time 

		sys.stdout.write("\033[F\033[F\033[F\033[F\033[F\033[F")
		sys.stdout.write("Missions simulated: " + str(t + 1))
		sys.stdout.write("\nTimes died: " + str(deaths))
		sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
		sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
		sys.stdout.write("\nAverage days survived: " + str( cum_days_survived / (t+1)))
		sys.stdout.write("\nLongest mission: " + str(max_days_survived))
		sys.stdout.write("\n...")
		sys.stdout.flush()

	print("\nSampled probability of mission success: " + str(1 - deaths/float(trials)))