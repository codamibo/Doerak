import numpy as np

def draw_cards(src, dest, n):
	cards = np.random.choice(range(len(src)), n, replace = False)
	dest = np.append(dest, src[cards])
	src = np.delete(src, cards)
	return src, dest