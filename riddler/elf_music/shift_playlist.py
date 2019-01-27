#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/santa-needs-some-help-with-math/
"""

import numpy
import time
import sys
import math

# Function to simulate the songs the elves would hear in a single shift
def shift_simulator(playlist_size):
	songs_played = list()

	# Playing 100 songs randomly from the playlist given the playlist_size
	for song_no in range(1, 100):

		# Picking random song to play next
		song = numpy.random.randint(1, playlist_size)
	
		# If the song has been played then break and return failure to break snowballs!
		# Else add the specific song to the list of songs that have been played so far this shift
		if song in songs_played:
			return False
		else:
			songs_played.append(song)

	# If we make it through the list then return success of shift without snowballs!
	return True

# Main simulation function
if __name__=='__main__':

	# Recording simulation input from user
	start_time = time.time()
	playlist_size_l = int(raw_input("Size of playlist (low)? "))
	playlist_size_h = int(raw_input("Size of playlist (high)? "))
	trials = int(raw_input("How many shift simulations do you want to run for each playlist size? "))

	# Running trials of varying playlist sizes
	for playlist_size in range(playlist_size_l, playlist_size_h):

		# Failure count
		snowballed = 0
		print("...")
		sys.stdout.write("\n\n\n\n")

		# Run the set of trials for the given playlist size
		for t in range(0,trials):

			# Call shift simulator
			safe_shift = shift_simulator(playlist_size)

			# Record number of failures
			if not safe_shift:
				snowballed += 1

			run_time = time.time() - start_time 

			# Live output of stats and estimated simulation time
			sys.stdout.write("\033[F\033[F\033[F\033[F")
			sys.stdout.write("Shifts worked: " + str(t + 1))
			sys.stdout.write("\nSnowballed Shifts: " + str(snowballed))
			sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
			sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
			sys.stdout.write("\n...")
			sys.stdout.flush()
		
		# Print final empirical probability of failure to prevent snowballs with given playlist size
		print("\nSampled probability of snowballed Shifts: " + str(snowballed/float(trials)) + " Playlist size: " + str(playlist_size))