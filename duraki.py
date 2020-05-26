import numpy as np
import durak_helpers as dk
import math
SIZE_DECK = 36

# deck		0
# player1	1
# player2	2
# board		3
# bin		4
# 0 1 2 3 4  5 6 7 8 
# 6 7 8 9 10 B V K A


deck = np.array(['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8',
                'K0', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8',
                'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8',
                'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'])

# deck = np.array(['H0', 'H1', 'H2',
#                 'K0', 'K1', 'K2', 
#                 'R0', 'R1', 'R2', 'R3',
#                 'S0', 'S1', 'S2', 'S4'])

print('Deck:')
print(deck)
print(" ")
player1 = np.array([])
player2 = np.array([])
kozur = np.array([])

deck, player1 = dk.draw_cards(deck, player1, 6)
deck, player2 = dk.draw_cards(deck, player2, 6)
deck, kozur = dk.draw_cards(deck, kozur, 1)
kozur_type = kozur[0][0]

print('Player 1: ')
print(player1)
print("")
print("Player 2: ")
print(player2)
print("")
print("Deck:")
print(deck)
print(" ")
print("Kozur:")
print(kozur)
print(kozur_type)

turn = 0
lowest = '9'
lowest_p1 = '9'
lowest_p2 = '9'

for card in range(len(player1)):
	if player1[card][0] == kozur_type:
		if player1[card][1] < lowest:
			turn = 1
			lowest = player1[card][1]
	elif player1[card][1] < lowest_p1:
		lowest_p1 = player1[card][1]     

	if player2[card][0] == kozur_type:
		if player2[card][1] < lowest:
			turn = 2
			lowest = player2[card][1]
	elif player2[card][1] < lowest_p2:
		lowest_p2 = player2[card][1]   

if turn == 0:
    if lowest_p1 < lowest_p2:
        turn = 1
    elif lowest_p2 < lowest_p1:
        turn = 2		
    else:
        turn = np.random.choice([1,2])
print(" ")
print("Turn: ")
print(turn)
print("Lowest: ")
print(lowest)
print(lowest_p1)
print(lowest_p2)

total = 0

while len(player1) and len(player2):
	previous_turn = turn
	player1, player2, deck, turn = dk.game_turn(player1, player2, deck, turn, kozur_type)
	if len(player1) == 0 and len(player2) > 0:
		print('Player one wins!')
		break
	elif len(player2) == 0 and len(player1) > 0:
		print('Player two wins!')
		break
	elif len(player1) == 0 and len(player2) == 0:
		print('The game is a draw!')
		break
	elif len(kozur):
		player1, player2, deck, kozur = dk.fill_hands(player1, player2, deck, kozur, previous_turn)




# 	if 6 - len(player1) > 0 and 6 - len(player2) > 0:
# 		if (6 - len(player1) + 6 - len(player2)) > len(deck) + 1:
# 			total = len(player1) + len(player2) + len(deck) + 1
# 			if (turn == 1):
# 				deck, player1 = dk.draw_cards(deck, player1, math.floor(total/2))
# 				deck, player2 = dk.draw_cards(deck, player2, len(deck))
# 				deck, player2 = dk.draw_cards(kozur, player2, 1)
# 			else:
# 				deck, player2 = dk.draw_cards(deck, player2, math.floor(total/2))
# 				deck, player1 = dk.draw_cards(deck, player1, len(deck))
# 				deck, player1 = dk.draw_cards(kozur, player1, 1)
# 		else:
# 			deck, player1 = dk.draw_cards(deck, player1, 6 - len(player1))
# 			deck, player2 = dk.draw_cards(deck, player2, 6 - len(player2))
# 	elif 6 - len(player1) > len(deck):
# 		deck, player1 = dk.draw_cards(deck, player1, len(deck))
# 	elif 6 - len(player2) > len(deck):
# 		deck, player2 = dk.draw_cards(deck, player2, len(deck))
# 	else:
# 		deck, player1 = dk.draw_cards(deck, player1, max(6 - len(player1), 0))
# 		deck, player2 = dk.draw_cards(deck, player2, max(6 - len(player2), 0))