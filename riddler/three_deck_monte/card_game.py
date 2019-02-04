#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/can-you-escape-a-maze-without-walls/
"""

import numpy
import time
import sys
import math

# Player class contains the label of the deck that the player will play, and conrtucts the deck given the color.  
# Also includes the number of rounds won per player
# Input should be a string which is the deck color
class player:
	deck = list()
	deck_label = str()
	wins = int()

	# Constructor taking the deck_label and building the proper deck based on color input
	def __init__(self, deck_label):
		if deck_label == "Red" or deck_label == "RED" or deck_label == "red" or deck_label == "r" or deck_label == "R":
			self.deck = [14, 14, 14, 14, 9, 9, 9, 9, 7, 7, 7, 7]
		elif deck_label == "Blue" or deck_label == "BLUE" or deck_label == "blue" or deck_label == "b" or deck_label == "B":
			self.deck = [13, 13, 13, 13, 11, 11, 11, 11, 6, 6, 6, 6]
		elif deck_label == "Black" or deck_label == "BLACK" or deck_label == "black" or deck_label == "bk" or deck_label == "BK":
			self.deck = [12, 12, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8]
		else:
			raise Exception("Player did not receive a proper deck type")

# Inputs are the decks for each player and the number of face-offs to win the game
def game_simulator(player1, player2, to_win):
	while True:

		# Draw a card randomly from each deck and pop it from the list (without replacement draw)
		card1 = player1.deck.pop(numpy.random.randint(0, len(player1.deck)))
		card2 = player2.deck.pop(numpy.random.randint(0, len(player2.deck)))

		if (card1 > card2):
			player1.wins += 1
			if player1.wins == to_win: return 1
		else:
			player2.wins += 1
			if player2.wins == to_win: return 2

if __name__=='__main__':
	start_time = time.time()

	deck_possible_inputs = ["Red", "RED", "red", "r", "R", "Blue", "BLUE", "blue", "b", "B", "Black", "BLACK", "black", "bk", "BK"]

	# User input values for chosen decks, win requirement, and number of games to simulate
	deck1 = str(raw_input("What deck does player 1 choose? "))
	if deck1 not in deck_possible_inputs:
		raise Exception("Please enter the proper color or number deck.  Options are red, blue, black")

	deck2 = str(raw_input("What deck does player 2 choose? "))
	if deck2 not in deck_possible_inputs:
		raise Exception("Please enter the proper color or number deck.  Options are red, blue, black")

	to_win = int(raw_input("What how many face-offs must be won to win the game? "))
	trials = int(raw_input("How many games do you want to simulate? "))

	print("...")
	sys.stdout.write("\n\n\n\n\n")

	# Initial values for missions failed, missions succeeded, total days survived in all missions, and the longest mission before failure
	player1_victories = 0
	player2_victories = 0

	# Simulating games
	for t in range(0,trials):
		player1 = player(deck1)
		player2 = player(deck2)

		# Call game simulator with parameters specific player classes and the win condition for each game
		victory = game_simulator(player1, player2, to_win)

		# Gathering how many times each player won the game with their respective decks
		if victory == 1:
			player1_victories += 1
		else:
			player2_victories += 1

		run_time = time.time() - start_time 

		# Output data
		sys.stdout.write("\033[F\033[F\033[F\033[F\033[F")
		sys.stdout.write("Games simulated: " + str(t + 1))
		sys.stdout.write("\nPlayer 1 victories " + "(" + deck1 + " deck): " + str(player1_victories))
		sys.stdout.write("\nPlayer 2 victories " + "(" + deck2 + " deck): " + str(player2_victories))
		sys.stdout.write("\nRun time: " + str(math.floor(run_time * 10) / 10) + " seconds     ")
		sys.stdout.write("\nEstimated time remaining: " + str(math.floor((trials*run_time / (t+1) - run_time)*10) / 10) + " seconds     ")
		sys.stdout.write("\n...")
		sys.stdout.flush()

	# Final output of empirical chance each player victory
	print("\nSampled probability of player 1 victory " + "(" + deck1 + " deck): " + str(player1_victories/float(trials)))
	print("\nSampled probability of player 2 victory " + "(" + deck2 + " deck): " + str(player2_victories/float(trials)))