# Scoring functions
def digs(dice, num):
	score = 0
	for i in dice:
		if i == int(num):
			score += int(num)
	return score

def threek(dice):
	score = 0
	for i in dice:
		if dice.count(i) >= 3:
			score = sum(dice)
			return score
		else:
			return score
	
def fourk(dice):
	score = 0
	for i in dice:
		if dice.count(i) >= 4:
			score = sum(dice)
			return score
		else:
			return score
			
def fullhouse(dice):
	score = 0
	dice = sorted(set(dice))
	if len(dice) == 2:
		score = 25
		return score
	else:
		return score
		
def smlstrt(dice):
	score = 0
	dice = str(sorted(dice))

	if "1, 2, 3, 4" in dice:
		score = 30
		return score
	elif "2, 3, 4, 5" in dice:
		score = 30
		return score
	elif "3, 4, 5, 6" in dice:
		score = 30
		return score
	else:
		return score
		
def lrgstrt(dice):
	score = 0
	dice = str(sorted(set(dice)))
	if "[1, 2, 3, 4, 5]" in dice:
		score = 40
		return score
	elif "[2, 3, 4, 5, 6]" in dice:
		score = 40
		return score
	else:
		return score
	
def yahtzee(dice):
	score = 0
	count = 0
	for i in dice:
		if dice[i] == dice[i + 1]:
			count += 1
		else:
			pass
	if count == 5:
		score = 50
		return score
	else:
		return score
		
def chance(dice):
	score = sum(dice)
	return score