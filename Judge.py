def judge(Grade1, Grade2):
	if Grade1[0] > Grade2[0]:
		return 1
	if Grade1[0] == Grade2[0] and Grade1[1] > Grade2[1]:
		return 1
	if Grade1[0] == Grade2[0] and Grade1[1] == Grade2[1]:
		return 0
	if (Grade1[0] > Grade2[0]) == False and (Grade1[0] == Grade2[0] and Grade1[1] > Grade2[1]) == False and (Grade1[0] == Grade2[0] and Grade1[1] == Grade2[1]) == False:
		return 2

