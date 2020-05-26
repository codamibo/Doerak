import numpy as np
import math

def draw_cards(src, dest, n):
	if n > 0:
		cards = np.random.choice(range(len(src)), int(n), replace = False)
		print('cards', cards)
		for i in cards:
			dest = np.append(dest, src[i])
		src = np.delete(src, cards)
	return src, dest

def	valid_attack(player, table):
	valid_cards = []
	for i in range(len(player)):
		for j in range(len(table)):
			if (table[j][1] == player[i][1]):
				valid_cards.append(i)
	return valid_cards


def	valid_defense(player, to_defend, kozur):
	valid_cards = []
	for i in range(len(player)):
		if to_defend[0] != kozur:
			if ((to_defend[1] < player[i][1]) and to_defend[0] == player[i][0]) or player[i][0] == kozur:
				valid_cards.append(i)
		elif ((to_defend[1] < player[i][1]) and to_defend[0] == player[i][0]):
			valid_cards.append(i)
	return valid_cards

def inputNumber(valid_cards):
	while True:
		try:
			card_index = int(input())       
		except ValueError:
			print("Not an integer! Try again.")
			continue
		else:
			if card_index in valid_cards or card_index == -1:
				return card_index
			print("Not a valid card! Try again.")
			continue

def inputNumber_empty(player):
	while True:
		try:
			card_index = int(input())       
		except ValueError:
			print("Not an integer! Try again.")
			continue
		else:
			if card_index > -1 and card_index < len(player):
				return card_index
			print("Number not in hand! Try again.")
			continue

def game_turn(player1, player2, deck, turn, kozur_type):
	# player 1: cards of player 1
	# player 2: cards of player 2
	# deck: cards remaining in the deck
	# turn: 1 if player 1 is attacking, 2 if player 2 is attacking

	table = []
	valid_cards_at = []
	valid_cards_def = []
	players = [player1, player2]
	attacker_index = (turn + 1) % 2
	defender_index = turn % 2
	while len(player1) and len(player2):
		#attacker
		print('deck', deck)
		print('table', table)
		print('Your choice: ', players[attacker_index])
		if len(table) > 0:
			print('For aboy type -1\n')
			valid_cards_at = valid_attack(players[attacker_index], table)
			print('valid cards attack', valid_cards_at)
			card_index = inputNumber(valid_cards_at)
			if card_index == -1:
				return players[0], players[1], deck, (turn % 2) + 1	
		else:
			card_index = inputNumber_empty(players[attacker_index])
		table.append(players[attacker_index][card_index])
		players[attacker_index] = np.delete(players[attacker_index], card_index)

		# defender
		print('deck', deck)
		print('table', table)
		print('Your options: ', players[defender_index])
		valid_cards_def = valid_defense(players[defender_index], table[-1], kozur_type)
		print('valid def options', valid_cards_def)
		card_index = input('For surrender type -1\n Your choice: ')
		while card_index not in valid_cards_def and card_index != -1:
			print('Not a valid move! Try again!')
			card_index = input('For surrender type -1\n Your choice: ')
		if card_index == -1:
			table, players[defender_index] = draw_cards(table, players[defender_index], len(table))
			return players[0], players[1], deck, turn
		table.append(players[defender_index][card_index])
		players[defender_index] = np.delete(players[defender_index], card_index)
	return players[0], players[1], deck, turn
	
def fill_hands(player1, player2, deck, kozur, previous_turn):
	n_1 = 0
	n_2 = 0
	take_kozur = 0
	total = 0
	pp = 0
	draw_start = 1
	if len(deck) + 1 <= max(6 - len(player1), 0) + max(6 - len(player2), 0):
		total = len(player1) + len(player2) + len(deck) + 1
		pp = float(total) / 2.
		if previous_turn == 1 and len(player2) < pp:
			take_kozur = 2
			draw_start = 1
		elif previous_turn == 2 and len(player1) < pp:
			take_kozur = 1 
			draw_start = 2
		elif (previous_turn == 1):
			take_kozur = 1
			draw_start = 2
		else:
			take_kozur = 2
			draw_start = 1
		while n_1 + n_2 < len(deck):
			if draw_start == 1 and len(player1) < pp:
				n_1 += 1
			elif draw_start == 2 and len(player2) < pp:
				n_2 += 1
			if len(player1) < len(player2):
				draw_start = 1
			else:
				draw_start = 2
		deck, player1 = draw_cards(deck, player1, n_1)
		deck, player2 = draw_cards(deck, player2, n_2)
		if take_kozur == 2:
			kozur, player2 = draw_cards(kozur, player2, 1)
		elif take_kozur == 1:
			kozur, player1 = draw_cards(kozur, player1, 1)
	elif len(deck) >= max(6 - len(player1), 0) + max(6 - len(player2), 0):
		n_1 = max(6 - len(player1), 0)
		n_2 = max(6 - len(player2), 0)
		deck, player1 = draw_cards(deck, player1, n_1)
		deck, player2 = draw_cards(deck, player2, n_2)	
	
	return player1, player2, deck, kozur