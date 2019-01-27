#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/the-eternal-question-how-much-do-these-apricots-weigh/
"""

import numpy


# Initial variables for number of wins and the win the required the most flips
win_count = 0
largest_win = 0

# Simulating number of game trials
for trials in range(1,10000000):

	# Initially it requires one flip of heads to win
	to_win = 1
	count = 0

	# Simulation of the individual game
	for i in range(1,1000):
		# Flip the coin
		flip = numpy.random.binomial(1, 0.5)

		# If flip is heads then increase the count
		if flip == 1:
			count += 1

			# If numbers of heads in a row matches the win condition then win and break from game
			if count == to_win: 
				win_count += 1

				# Record the largest flip count to win
				if count > largest_win:
					largest_win = count
				
				break

		# If the flip is tails then the number of heads to win increases for the next series of flips. Reset head count
		else:
			count = 0
			to_win += 1

# Printing empirical win probability and the largest flips to win
print(win_count/10000000.0)
print(largest_win)