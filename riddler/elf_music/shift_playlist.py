#!/usr/bin/env python

import numpy
import time
import sys
import math

def shift_simulator(playlist_size):
	songs_played = list()

	for song_no in range(1, 100):

		song = numpy.random.randint(1, playlist_size)
	
		if song in songs_played:
			return False
		else:
			songs_played.append(song)

	return True

if __name__=='__main__':
	start_time = time.time()
	playlist_size_l = int(raw_input("Size of playlist (low)? "))
	playlist_size_h = int(raw_input("Size of playlist (high)? "))
	trials = int(raw_input("How many shift simulations do you want to run? "))


	for playlist_size in range(playlist_size_l, playlist_size_h):

		snowballed = 0
		print("...")
		# sys.stdout.write("\n\n\n\n")

		for t in range(0,trials):

			safe_shift = shift_simulator(playlist_size)
			if not safe_shift:
				snowballed += 1

			run_time = time.time() - start_time 

			# sys.stdout.write("\033[F\033[F\033[F\033[F")
			# sys.stdout.write("Shifts worked: " + str(t + 1))
			# sys.stdout.write("\nSnowballed Shifts: " + str(snowballed))
			# sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
			# sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
			# sys.stdout.write("\n...")
			sys.stdout.flush()
		
		print("\nSampled probability of snowballed Shifts: " + str(snowballed/float(trials)) + " Playlist size: " + str(playlist_size))