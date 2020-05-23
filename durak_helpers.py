import numpy as np

def draw_cards(src, dest, n):
	cards = np.random.choice(range(len(src)), n, replace = False)
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

	turn = 1
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
		print('Your options: ', players[attacker_index])
		if len(table) > 0:
			valid_cards_at = valid_attack(players[attacker_index], table)
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
		card_index = input('For surrender type -1\n Your choice: ')
		while card_index is int and card_index not in valid_cards_def and card_index != -1:
			print('Not a valid move! Try again!')
			card_index = input('For aboy type -1\n Your choice: ')
		if card_index == -1:
			table, players[defender_index] = draw_cards(table, players[defender_index], len(table))
			return players[0], players[1], deck, turn
		table.append(players[defender_index][card_index])
		players[defender_index] = np.delete(players[defender_index], card_index)

	return players[0], players[1], deck, turn
	
