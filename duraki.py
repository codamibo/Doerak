import numpy as np
import durak_helpers as dk

SIZE_DECK = 32

# deck		0
# player1	1
# player2	2
# board		3
# bin		4

deck = np.array(['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7',
                'K0', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7',
                'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7',
                'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7'])

# np.random.shuffle(deck)
print('Deck:')
print(deck)
print(" ")
player1 = np.array([])
player2 = np.array([])
kozur = np.array([])

deck, player1 = dk.draw_cards(deck, player1, 7)
deck, player2 = dk.draw_cards(deck, player2, 7)
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
lowest = '8'
lowest_p1 = '8'
lowest_p2 = '8'

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