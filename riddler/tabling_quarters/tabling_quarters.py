#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/i-would-walk-500-miles-and-i-would-riddle-500-more/
"""

import numpy
import rospy
import numpy
import time
import sys
import math

class tabling_quarters:

	def __init__(self, steps, flip_cmd):
		self.quarter_states = [numpy.random.randint(0,2) for i in range(0,4)]
		win = False
		reorg_quarts = list()
		step_num = 0
		# flip_cmd = 1
		self.turns = 0
		while True:
			win = self.check_win()
			
			if win:
				# print("You win! GG")
				# print("Total turns: " + str(turns))
				break
			# self.print_table()

			self.flip_quaters(flip_cmd[step_num])
			
			if step_num < steps - 1:
				step_num += 1
			else:
				step_num = 0
							
			self.check_win()
			
			if win:
				# print("You win! GG")
				# print("Total turns: " + str(turns))
				break
			# self.print_table()

			reorg_quarts = self.spin_table()
			self.quarter_states = reorg_quarts
			self.turns += 1
			if self.turns > 999: break


	def flip_quaters(self, quart_str):
		flips_list = quart_str.split()
		
		for i in flips_list:
			if self.quarter_states[int(i)-1] == 1:
				self.quarter_states[int(i)-1] = 0
			else:
				self.quarter_states[int(i)-1] = 1

	def spin_table(self):
		spin = numpy.random.randint(-4,0)
		return [self.quarter_states[i+spin] for i in range(0,4)]

	def check_win(self):
		
		for i in self.quarter_states:
			
			if i == 0:
				return False

		return True

	def print_table(self):

		print("")
		print(" (" + str(self.quarter_states[0]) + ") ----- (" + str(self.quarter_states[1]) + ") ")
		print("  |         |  ")
		print("  |         |  ")
		print("  |         |  ")
		print(" (" + str(self.quarter_states[3]) + ") ----- (" + str(self.quarter_states[2]) + ") ")
		print("")

if __name__=='__main__':
	
	steps = int(raw_input("How many steps does your strategy take until it repeats? "))
	flip_cmd = list()
	print("---")
	print("For your next set of inputs enter the specific coins you would like to flip over (1-4).")
	print("Each coin has an assigned location.  1 meaning the far left corner of the table, 2 meaning the far right, 3 means the near right, and 4 means the near left.")
	print("You may enter as few a 1 coin or as many as 4.")
	print("Separate each coin you want to flip with a space")
	print("Example: I want to flip coins 1, 2, and 4 over.  The command to enter is: 1 2 4")
	print("---")
	for i in range(0, steps):
		flip_cmd.append(str(raw_input("Please enter your next step in the strategy.  Enter the number coin(s) you would like to flip over (1-4) and separate each coin by a space: ")))
		
	trials = int(raw_input("How many trial games would you like to simulate? "))
	print("simulating...")
	turn_data = []
	for t in range(0, trials):
		TablingQuarters = tabling_quarters(steps, flip_cmd)

		turn_data.append(TablingQuarters.turns)

	print("")
	print("--- RESULTS ---")
	print("Turn median: " + str(numpy.median(turn_data)))
	print("Turn mean: " + str(numpy.mean(turn_data)))
	print("Stdev: " + str(numpy.std(turn_data)))
	print("Max: " + str(numpy.max(turn_data)))