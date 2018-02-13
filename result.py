def result(action1p, action2p, winnerp):
	global resultB
	global winner
	money1 = -10
	money2 = -10
	deltamoney = 10
	moneypond = 20
	# i = 0
	# action1 = []
	# for item in action1p:
	# 	if item == 0:
	# 		action1[i] = 'open'
	# 	if item == 1:
	# 		action1[i] = 'follow'
	# 	if item == 2:
	# 		action1[i] = 'doublefollow'
	# 	if item == 3:
	# 		action1[i] = 'discard'
	# 	i = i + 1

	# j = 0 
	# action2 = []
	# for item in action2p:
	# 	if item == 0:
	# 		action2[j] = 'open'
	# 	if item == 1:
	# 		action2[j] = 'follow'
	# 	if item == 2:
	# 		action2[j] = 'doublefollow'
	# 	if item == 3:
	# 		action2[j] = 'discard'
	# 	j = j + 1


# 0 discard 1 follow 2 doublefollow 3 open



	for round in [0, 1, 2]:
	#for round in [0, 1, 2, 3, 4]:

		action1 = action1p[round]
		# print ('player1 took: %s' %(action1))
		

		if action1 == 0:
			winner = 2
			break

		if action1 == 3:
			money1 = money1 - 2*deltamoney
			moneypond = moneypond + 2*deltamoney
			winner = winnerp
			break

		action2 = action2p[round]
		# print ('player2 took: %s' %(action2))


		if action1 == 1 and action2 == 0:
			money1 = money1 - deltamoney
			moneypond = moneypond + deltamoney
			winner = 1
			break
		if action1 == 1 and action2 == 3:
			money1 = money1 - deltamoney
			money2 = money2 - 2*deltamoney
			moneypond = moneypond + deltamoney + 2*deltamoney
			winner = winnerp
			break
		if action1 == 1 and action2 == 1:
			money1 = money1 - deltamoney
			money2 = money2 - deltamoney
			moneypond = moneypond + deltamoney + deltamoney
		if action1 == 1 and action2 == 2:
			money1 = money1 - deltamoney
			money2 = money2 - 2*deltamoney
			moneypond = moneypond + deltamoney + 2*deltamoney
			deltamoney = 2 * deltamoney

		if action1 == 2 and action2 == 3:
			money1 = money1 - 2*deltamoney
			money2 = money2 - 4*deltamoney
			moneypond = moneypond + 2*deltamoney + 4*deltamoney
			winner = winnerp
			break
		if action1 == 2 and action2 == 0:
			money1 = money1 -2*deltamoney
			moneypond = moneypond + 2*deltamoney
			winner = 1
			break
		if action1 == 2 and action2 == 2:
			money1 = money1 - 2*deltamoney
			money2 = money2 - 4*deltamoney
			moneypond = moneypond + 2*deltamoney + 4*deltamoney
			deltamoney = 4*deltamoney
		if action1 == 2 and action2 == 1:
			money1 = money1 - 2*deltamoney
			money2 = money2 - 2*deltamoney
			moneypond = moneypond + 2*deltamoney + 2*deltamoney
			deltamoney = 2*deltamoney
		# if action1 == 'follow' and action2 == 'discard':
		# 	money1 = money1 - deltamoney
		# 	moneypond = moneypond + deltamoney
		# 	winner = 1
		# if action1 == 'follow' and action2 == 'open':
		# 	money1 = money1 -deltamoney
		# 	money2 = money2 -2*deltamoney
		# 	moneypond = moneypond + deltamoney + 2*deltamoney
		# 	winner = winnerp
		# 	break
		# if action1 == 'follow' and action2 == 'follow':
		# 	money1 = money1 - deltamoney
		# 	money2 = money2 - deltamoney
		# 	moneypond = moneypond + deltamoney + deltamoney
		# if action1 == 'follow' and action2 == 'doublefollow':
		# 	money1 = money1 - deltamoney
		# 	money2 = money2 - 2*deltamoney
		# 	moneypond = moneypond + deltamoney + 2*deltamoney
		# 	deltamoney = 2*deltamoney


		i = round
		if i == 2:
			winner = winnerp

	# print (moneypond)
	# print (money1)
	# print (money2)
	# print (deltamoney)

	# print
	# print('results:')
	if winner == 1:
		# print ('winner is player1, he or she winned %d dollars' %(money1 + moneypond))
		# print ('loser is player2, he or she lost %d dollars' %(-money2))
		resultA = money1 + moneypond
		resultB = money2
	if winner == 2:
		# print ('winner is player2, he or she winned %d dollars' %(money2 + moneypond))
		# print ('loser is player1, he or she lost %d dollars' %(-money1))
		resultA = money1
		resultB = money2 + moneypond

	return resultB

