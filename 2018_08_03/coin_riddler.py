#!/usr/bin/env python

import numpy

win_count = 0
largest_win = 0

for trials in range(1,10000000):
	to_win = 1
	count = 0

	for i in range(1,1000):
		flip = numpy.random.binomial(1, 0.5)

		if flip == 1:
			count += 1

			if count == to_win: 
				win_count += 1
				if count > largest_win:
					largest_win = count
				break
		else:
			count = 0
			to_win += 1

print(win_count/10000000.0)
print(largest_win)