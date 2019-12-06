#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/how-fast-can-you-skip-to-your-favorite-song/
"""

import numpy

dist = int(raw_input('Please enter the distance away from the song that you would like to just use "Next" to get to.: '))
trials = int(raw_input('Please enter the number of trials you want to conduct for this test: '))
playlist = list(range(1,101))
data = list()
for i in range(0,trials):
	newsong = numpy.random.randint(1,101)
	num_presses = 0

	while (newsong > 42) or ((newsong + dist) < 42):
		newsong = numpy.random.randint(1,101)
		num_presses += 1

	num_presses += 42 - newsong

	data.append(num_presses)

print("")
print("--- RESULTS ---")
print("Turn median: " + str(numpy.median(data)))
print("Turn mean: " + str(numpy.mean(data)))
print("Stdev: " + str(numpy.std(data)))
print("Max: " + str(numpy.max(data)))