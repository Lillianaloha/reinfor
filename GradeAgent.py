import numpy as np
import random
def GradetheAgent():
	a = random.randrange(1, 273)
	if a == 1:
		level = 6
		rank = random.randrange(2, 15)
	if a == 2:
		level = 5
		rank = random.randrange(2, 15)
	if a > 2 and a < 131:
		level = 4
		rank = random.randrange(703, 2376)
	if a > 130 and a < 259:
		level = 1
		rank = random.randrange(703, 2376)
	if a > 258 and a < 272:
		level = 2
		rank = random.randrange(15, 182)
	if a == 272:
		level = 3
		rank = random.randrange(4, 15)
	return level, rank

