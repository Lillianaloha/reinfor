def genact1(level1, rank1):
	if level1 == 1 and rank1 < 2591:
		action111=(1,0,0,0,0)
	if level1 == 1 and rank1 >2590:
		action111=(2,0,0,0,0)
	if level1 == 2 and rank1 <141:
		action111=(1,2,0,0,0)
	if level1 == 2 and rank1 >140:
		action111=(1,1,1,0,0)
	if level1 == 3 or level1 == 4:
		action111=(1,2,1,0,0)
	if level1 == 5 or level1 == 6:
		action111=(1,1,2,0,0)
	return action111

def genact2(level1, rank1):
	if level1 == 1 and rank1 < 2591:
		action111=(1,1,0,0,0)
	if level1 == 1 and rank1 >2590:
		action111=(2,1,0,0,0)
	if level1 == 2 and rank1 <141:
		action111=(2,1,0,0,0)
	if level1 == 2 and rank1 >140:
		action111=(2,2,0,0,0)
	if level1 == 3 or level1 == 4:
		action111=(1,2,2,0,0)
	if level1 == 5 or level1 == 6:
		action111=(2,2,2,0,0)
	return action111

def genact3(level1, rank1):
	if level1 == 1 and rank1 < 2591:
		action111=(1,2,1,0,0)
	if level1 == 1 and rank1 >2590:
		action111=(2,1,1,0,0)
	if level1 == 2 and rank1 <141:
		action111=(2,2,1,0,0)
	if level1 == 2 and rank1 >140:
		action111=(1,2,2,0,0)
	if level1 == 3 or level1 == 4:
		action111=(1,1,2,0,0)
	if level1 == 5 or level1 == 6:
		action111=(1,1,1,0,0)


	return action111
