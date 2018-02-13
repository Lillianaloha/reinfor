# g=[[],[],[],[]]
# #a[1][2][3][4]=1
# for i in range(4):
# 	for j in range(4):
# 		for a in range(4):
# 			for b in range(4):
# 				a[i][j][a][b] = 
# print (g)
import random
import numpy as np
from result import *
from Judge import *
from GradetheCard import *
import time
from GenAct import *
from GradeAgent import *
start = time.clock()


#w, h, radius = 5, 10, 10
# for action11 in range(4):
# 	stateaction11 = {}
# 	for action12 in range(4):
# 		stateaction12 = {}
# 		for action21 in range(4):
# 			stateaction21 = {}
# 			for action22 in range(4):
# 				stateaction22 = {}
# 				for action31 in range(4):
# 					stateaction31 = {}
# 					for action32 in range(4):
# 						stateaction32 = {}
# 						for action41 in range(4):
# 							stateaction41 = {}
# 							for action42 in range(4):
# 								stateaction42 = {}
# 								for action51 in range(4):
# 									stateaction51 = {}
# 									for action52 in range(4):
# 										stateaction52 = {}
# 										for level in range(6):
# 											levelrank = {}
# 											for rank in range(52*52*52):
# 												levelrank[rank] = i
# 												i = i + 1
# 											stateaction52[level] = levelrank
# 										stateaction51[action52] = stateaction52
# 									stateaction42[action51] = stateaction51
# 								stateaction41[action42] = stateaction42
# 							stateaction32[action41] = stateaction41
# 						stateaction31[action32] = stateaction32
# 					stateaction22[action31] = stateaction31
# 				stateaction21[action22] = stateaction22
# 			stateaction12[action21] = stateaction21
# 		stateaction11[action12] = stateaction12
# 	stateaction[action11] = stateaction11
i = 1
state2 = {}
#for pot in range(10, 10230, 10):
##########################
#state
for pot in range(10, 640, 10):

	potlist = {}
	#for R in range(0, 5):
	for R in range(0, 3):
		roundlist = {}
		#for delta in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]:
		for delta in [10, 20, 40, 80, 160, 320]:
			deltalist = {}
			for level in range(1, 7):
				levellist = {}
				for rank in range(1, 2400):
					levellist[rank] = i
					i = i + 1
				deltalist[level] = levellist
			roundlist[delta] = deltalist
		potlist[R] = roundlist
	state2[pot] = potlist

elapsed = (time.clock() - start)
print("Time used:",elapsed)

# for a in range(5):

#  	for b in range(10):
#  		for c in range(10):
#  			hough[a][b][c]=1
# print (stateaction)

# position = np.argmax(stateaction)
# print (position)
def QLearning(num_episodes, e, gamma, lr, Q, GenerateAction1):
	
	for epi in range(0, num_episodes):
		
		i = 0
		done = False
		reward = 0
		action1 = {}
		action2 = {}
		Grade1, Grade2, player1, player2 = Grade()
		[level1, rank1] = Grade1
		# if level1 > 1:
		# 	action111 = (1, 1, 1, 1, 1)
		# if level1 == 1:
		# 	action111 = (1, 0, 0)
		[level, rank] = GradetheAgent()
		winnerp =  judge(Grade1, Grade2)
		action = (0, 1, 2, 3)
		#####################
		#taolu
		if GenerateAction1 == 1:
			action111 = genact1(level1, rank1)
		if GenerateAction1 == 2:
			action111 = genact2(level1, rank1)
		if GenerateAction1 == 3:
			action111 = genact3(level1, rank1)

	
		#action1[0] = random.choice(action)
		action1[0] = action111[0]
		pot = 30
		R = 0
		delta = 10

		if action1[0] == 0 or action1[0] == 3:
			done = True
			action2[0] = 0
			#reward = result(action1, action2, winnerp)
		if action1[0] == 1:
			pot = 10
			delta = 10
		if action1[0] == 2:
			pot = 20
			delta = 20
		state = state2[pot][R][delta][level][rank]



		while not done:
			if action1[i] == 0 or action1[i] == 3:
				reward = result(action1, action2, winnerp)
				Q[state][0] = Q[state][0] + lr*reward
				Q[state][1] = Q[state][1] + lr*reward
				Q[state][2] = Q[state][2] + lr*reward
				Q[state][3] = Q[state][3] + lr*reward
				break
			if action1[i] == 1 or action1[i] == 2:
				a = random.random()
				if a < 1-4/3*e:
					action2[i] = np.argmax(Q[state])
				else:
					action2[i] = random.choice(action)

				#action1[i+1] = random.choice(action)
				action1[i+1] = action111[i+1]

				QA = np.zeros(4)

				#if (action2[i] == 0 or action2[i] == 3) or R == 4:
				if (action2[i] == 0 or action2[i] == 3) or R == 2:
					reward = result(action1, action2, winnerp)
					Q[state][action2[i]] = Q[state][action2[i]] + lr*reward
					break

				if action2[i] == 1:
					if action1[i+1] == 1:
						pot = pot + 2*delta
					if action1[i+1] == 2:
						pot = pot + 3*delta
						delta = 2*delta
				if action2[i] == 2:
					if action1[i+1] == 1:
						pot = pot + 4*delta
						delta = 2*delta
					if action1[i+1] == 2:
						pot = pot + 6*delta
						delta = 4*delta

			statep = state2[pot][R][delta][level][rank]
			for actionp in range(0, 4):
				QA[actionp] = Q[statep][actionp]
			Q[state][action2[i]] = Q[state][action2[i]] + lr*(reward + gamma * max(QA) - Q[state][action2[i]])
			state = statep
			R = R + 1
			i = i + 1

		# if epi > 999900:
		# 	print(action2)
	return Q

		
	#print(action1)
	





		


Q = np.zeros((1360000000, 4))
Q = QLearning(10000000, 0.1, 0.9, 0.1, Q, 1)
Q = QLearning(10000000, 0.1, 0.9, 0.1, Q, 2)
Q = QLearning(1000000, 0.1, 0.9, 0.1, Q, 3)

for game in range(180):
	tol = 0
	for i in range(5):
		# print('the Game Begins')
		Grade1, Grade2, player1, player2 = Grade()
		# print('cards of Player1:')
		# print(player1)
		[level, rank] = Grade2
		winnerp =  judge(Grade1, Grade2)
		action = (0, 1, 2, 3)
		action1 = {}
		action2 = {}
		pot = 20 
		delta = 10
		#for R in range(0, 5):
		for R in range(0, 3):

			action1[R] = random.randint(0, 3)
			if action1[R] == 0 or action1[R] == 3:
				action2[R] = 0
				reward = result(action1, action2, winnerp)
				break
			if action1[R] == 1:
				pot = pot + delta
				state = state2[pot][R][delta][level][rank]
				action2[R] = np.argmax(Q[state])
				if action2[R] == 1:
					pot = pot + delta
				if action2[R] == 2:
					pot = pot + 2 * delta
					delta = 2 * delta


			if action1[R] == 2:
				pot = pot + 2 * delta
				delta = 2 * delta
				state = state2[pot][R][delta][level][rank]
				action2[R] = np.argmax(Q[state])
				if action2[R] == 1:
					pot = pot + delta
				if action2[R] == 2:
					pot = pot + 2 * delta
					delta = 2 * delta

			# print('action2:')
			# print(action2[R])
			if action2[R] == 0 or action2[R] == 3:
				reward = result(action1, action2, winnerp)
				break 
			if R ==2:
			#if R ==4:
				reward = result(action1, action2, winnerp)
			R = R + 1
		# print('cards of Player1:')
		# print(player1)
		# print('action of player1')
		# print(action1)
		# print('cards of Player2:')
		# print(player2)
		# print('action of player2:')
		# print(action2)
		# print('player2 wins:')
		# print(reward)
		tol = tol + reward
		i = i + 1
	print(tol)
	#print('winner:')





elapsed = (time.clock() - start)
print("Time used:",elapsed)












