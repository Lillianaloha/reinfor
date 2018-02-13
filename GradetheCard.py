#coding:utf-8
import random

def DealtheCard():

	#print
	cardList = [('H',14),('H',2),('H',3),('H',4),('H',5),('H',6),('H',7),
	            ('H',8),('H',9),('H',10),('H',11),('H',12),('H',13),
	            ('D',14),('D',2),('D',3),('D',4),('D',5),('D',6),('D',7),
	            ('D',8),('D',9),('D',10),('D',11),('D',12),('D',13),
	            ('S',14),('S',2),('S',3),('S',4),('S',5),('S',6),('S',7),
	            ('S',8),('S',9),('S',10),('S',11),('S',12),('S',13),
	            ('C',14),('C',2),('C',3),('C',4),('C',5),('C',6),('C',7),
	            ('C',8),('C',9),('C',10),('C',11),('C',12),('C',13)]

	cardRand = random.sample(cardList, 52)
	player1 = cardRand[0:3]
	player2 = cardRand[3:6]

	# print('cards of Player1:')
	# print(player1)
	# print('cards of Player2:')
	# print(player2)
	return player1, player2

def sequenceCheck(a, b, c):
	numList1 = [a, b, c]
	numList = sorted(numList1)
	if numList[2] - numList[1] == 1 and numList[1] - numList[0] == 1:
		return (True)
	else:
		return (False)
def coupleRank(a, b, c):
	d = [a, b, c]
	for item in d:
		if d.count(item) == 2:
			e = item
		if d.count(item) == 1:
			f = item
	rank = (e-1)*13 + f - 1
	return rank


def evaluator(handCards):
	if handCards[0][1] == handCards[1][1] and handCards[0][1] == handCards[2][1] and handCards[1][1] == handCards[2][1]:
		level = 6
		rank = handCards[1][1]
	if handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0] and sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1]):
		level = 5
		rank = max(handCards[0][1], handCards[1][1], handCards[2][1])
	if handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0] and sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1]) == False:
		level = 4
		rankpp = [handCards[0][1], handCards[1][1], handCards[2][1]]
		rankp = sorted(rankpp)
		rank = (rankp[2]-1)*13*13 + (rankp[1]-1)*13 + rankp[0] - 1
	if sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1]) and (handCards[0][0] != handCards[1][0] or handCards[0][0] != handCards[2][0] or handCards[1][0] != handCards[2][0]):
		level = 3
		rank = max(handCards[0][1], handCards[1][1], handCards[2][1])
	if (handCards[0][1] == handCards[1][1] or handCards[0][1] == handCards[2][1] or handCards[1][1] == handCards[2][1]) and ((handCards[0][1] == handCards[1][1] and handCards[0][1] == handCards[2][1] and handCards[1][1] == handCards[2][1]) == False) and ((handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0])==False):
		level = 2
		rank = coupleRank(handCards[0][1], handCards[1][1], handCards[2][1])
	if (handCards[0][1] == handCards[1][1] and handCards[0][1] == handCards[2][1] and handCards[1][1] == handCards[2][1]) == False and (handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0] and sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1])) == False and (handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0] and sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1]) == False) == False and (sequenceCheck(handCards[0][1], handCards[1][1], handCards[2][1]) and (handCards[0][0] != handCards[1][0] or handCards[0][0] != handCards[2][0] or handCards[1][0] != handCards[2][0])) == False and ((handCards[0][1] == handCards[1][1] or handCards[0][1] == handCards[2][1] or handCards[1][1] == handCards[2][1]) and ((handCards[0][1] == handCards[1][1] and handCards[0][1] == handCards[2][1] and handCards[1][1] == handCards[2][1]) == False) and ((handCards[0][0] == handCards[1][0] and handCards[0][0] == handCards[2][0] and handCards[1][0] == handCards[2][0])==False)) == False:
		level = 1
		rankpp = [handCards[0][1], handCards[1][1], handCards[2][1]]
		rankp = sorted(rankpp)
		rank = (rankp[2]-1)*13*13 + (rankp[1]-1)*13 + rankp[0] - 1
	return [level, rank]

def Grade():
	player1, player2 = DealtheCard()


	Grade1 = evaluator(player1)
	#print(Grade1)
	Grade2 = evaluator(player2)
	#print(Grade2)
	return Grade1, Grade2, player1, player2