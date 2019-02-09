#!/usr/bin/env python

"""
This code was written by Chris Suarez
as a contribution to fivethirtyeight.com.

This is a simultation to solve a problem posed
in the weekly segement called the riddler!

The link for this problem is here: 
https://fivethirtyeight.com/features/525600-minutes-of-math/
"""


import numpy
import time
import sys
import math

# Player class contains the players hand, all possible win conditions, and employed strategy
# Must pass is the strategy value employed...  
# 	Pass in 1 for player to play to maximize number of win conditions for themself
#	Pass in 2 for player to play to minimize number of win conditions for opponent
class player:

	def __init__(self, strategy):
		self.hand = []
		
		# There are only 8 initial win conditions
		self.win_conditions = [[1,5,9], [1,6,8], [2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]

		self.strat = strategy

# The pick card function takes in a player, the opponent, and the list of remaining cards in the pool
# The player and opponent must be of class player()
def pick_card(player, opponent, remaining_cards):
	# Initializing the list of counts that each card in the pool gets from employing a given strategy
	# This list is 9 members long which associate a count hit for each number in the card pool respectively
	plays_list = [0] * 9

	# Consider each card for the player in order of remaining cards
	for card in remaining_cards:

		# If the card wins the player the game then pick it
		for win_condition in player.win_conditions:
			if (card in win_condition) and (len(win_condition) == 1):
				print("player winning pick", card)
				return card

		# Else if the current card will win the game for your opponent next turn then pick it
		for win_condition in opponent.win_conditions:
			if (card in win_condition) and (len(win_condition) == 1):
				print("player survival pick", card)
				return card

		# Else employ strategy
		# Strategy 1 maximizes your possible number of win conditions
		if player.strat == 1:
			for win_condition in player.win_conditions:
				if card in win_condition:
					plays_list[card-1] += 1
		
		# Strategy 2 minimizes your opponents number of win conditions
		if player.strat == 2:
			for win_condition in opponent.win_conditions:
				if card in win_condition:
					plays_list[card-1] += 1

		# If your current strategy yields no cards to play then switch to other strategy
		if max(plays_list) == 0:

			# If there are no win conditions for you and you are playing strat 1 then look to thwart your opponent with strat 2
			if player.strat == 1:
				# Run strat 2
				for win_condition in opponent.win_conditions:
					if card in win_condition:
						plays_list[card-1] += 1

			# If there are no win conditions for your opponent and you are playing strat 2 then look to max your win conditions with strat 1
			elif player.strat == 2:
				# Strat 1
				for win_condition in player.win_conditions:
					if card in win_condition:
						plays_list[card-1] += 1

			# If there are no win conditions for you or your opponent then just pick the lowest card (likely the last remaining card)
			if max(plays_list) == 0:
				card = remaining_cards[0]

	# We want to play the card the has the most count hits.
	# It's possible that there are more than one card with the most count hits in a given scenario.  
	# In this case the code just choses the lowest card value.  (This may not be optimal, however.  I am unsure)
	card = plays_list.index(max(plays_list)) + 1
	return card

# The update players function updates the state of each player with respect to the card picked
# The player and their opponent must be passed in as an object of the player class
# Lastly the card that was picked from the pool must also be passed in as an integer
# The function returns a [player, opponent] list with new player and opponent data in the player class
def update_players(player, opponent, card_picked):

	# Adding the card to the hand of the player that picked the card
	player.hand.append(card_picked)

	# This loop removes the specific card from the set of win conditions for the player
	# For example, if [1,5,9] was a win condition and the player picked 1, then the new win condition is simply [5,9] 
	i = 0
	for win_condition in player.win_conditions:
		
		if card_picked in win_condition:
			player.win_conditions[i].remove(card_picked)
		i += 1

	# This loop removes the possible win conditions for the opponent given a card picked by the player
	# For example, if the opponent had multiple win conditions with card 1 in them then they are no longer viable win conditions for the opponent
	pop_list = []
	i = 0
	for win_condition in opponent.win_conditions:
		
		# Unfortunately we cannot simply pop the current win_condition from the list because it'll alter the for loop sequence
		# Must build a list of items to pop from the win_condition list instead and pop them in reverse order after this loop
		if card_picked in win_condition:
			pop_list.insert(0, i)
		i += 1

	# Popping win_conditions from opponent
	for i in pop_list:
		opponent.win_conditions.pop(i)

	return [player, opponent]

# The game simulator function manages the data for the game itself
# Players 1 and 2 must be passed in as an object of the player class
# The function keeps track of the remaining cards in the pool and calls the pick_card and update_player functions
# It returns a value of 1 if player 1 wins, 2 if player 2 wins, and 3 if the game ends in a draw 
def game_simulator(player1, player2):
	# Initializing the card pool
	remaining_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# Force pick first cards
	card_picked = 9
	remaining_cards.remove(card_picked)
	[player1, player2] = update_players(player1, player2, card_picked)

	# card_picked = 2
	# remaining_cards.remove(card_picked)
	# [player2, player1] = update_players(player2, player1, card_picked)

	while True:
		# If the players have the same hand size then it is player 1's turn
		if len(player1.hand) <= len(player2.hand):
			# Player1 picks a card
			card_picked = pick_card(player1, player2, remaining_cards)
			remaining_cards.remove(card_picked)
			[player1, player2] = update_players(player1, player2, card_picked)

			# Debug scripts
			print("player1", player1.hand, player1.win_conditions)
			print("player2", player2.hand, player2.win_conditions)
			print("remain cards", remaining_cards)
			
			# Check if player1 wins
			if len(player1.hand) >= 3:
				for i in range(0, len(player1.hand)):

					for j in range(0, len(player1.hand)):
						# Skip if j is the same card as i
						if (j == i): continue

						for k in range(0, len(player1.hand)):
							# Skip if k is the same card as i or j
							if (k == i or k == j): continue

							# Win condition check
							if ((player1.hand[i] + player1.hand[j] + player1.hand[k]) == 15): 
								print("player 1 wins", player1.hand)
								print("player 2 loses", player2.hand)
								return 1
		else:
			# Player2 picks a card
			card_picked = pick_card(player2, player1, remaining_cards)
			remaining_cards.remove(card_picked)
			[player2, player1] = update_players(player2, player1, card_picked)

			# Debug scripts
			print(player1.hand, player1.win_conditions)
			print(player2.hand, player2.win_conditions)

			# Check if player2 wins
			if len(player1.hand) >= 3:
				for i in range(0, len(player2.hand)):

					for j in range(0, len(player2.hand)):
						# Skip if j is the same card as i
						if (j == i): continue

						for k in range(0, len(player2.hand)):
							# Skip if k is the same card as i or j
							if (k == i or k == j): continue

							# Win condition check
							if ((player2.hand[i] + player2.hand[j] + player2.hand[k]) == 15): 
								print("player 2 wins", player2.hand)
								print("player 1 loses", player1.hand)
								return 2

		# If there are no remaining cards in the pool or if neither player has a possible win condition then the game is a draw
		if (len(remaining_cards) == 0) or (len(player1.win_conditions) == 0 and len(player2.win_conditions) == 0):
			print("game ends in draw")
			return 3

# Main function
if __name__=='__main__':

	# Initializing players to pass into game
	player1 = player(2) # Player 1 with strat 2
	player2 = player(2) # Player 2 with strat 2

	victor = game_simulator(player1,player2)
	print(victor)