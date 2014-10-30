import random
import scoring
from dice import Dice
from prettytable import PrettyTable

## Score card class to be used for multiple players
class Score(object):

	def __init__(self, name, score = 0):
		self.name = name
		self.score = score
		
	card = {"Ones" : None,
		"Twos" : None,
		"Threes" : None,
		"Fours" : None,
		"Fives" : None,
		"Sixes" : None,
		"Bonus" : None,
		"Three of a kind" : None,
		"Four of a kind" : None,
		"Full house" : None,
		"Small straight" : None,
		"Large straight" : None,
		"Yahtzee" : None,
		"Chance" : None,
		"Yahtzee bonus" : None}
	
	pretty_card = PrettyTable(["Category", "Score"])
	pretty_card.add_row(["Ones", card["Ones"]])
	pretty_card.add_row(["Twos", card["Twos"]])
	pretty_card.add_row(["Threes", card["Threes"]])
	pretty_card.add_row(["Fours", card["Fours"]])
	pretty_card.add_row(["Fives", card["Fives"]])
	pretty_card.add_row(["Sixes", card["Sixes"]])
	pretty_card.add_row(["Bonus", card["Bonus"]])
	pretty_card.add_row(["------------", "-"])
	pretty_card.add_row(["3 of a kind", card["Three of a kind"]])
	pretty_card.add_row(["4 of a kind", card["Four of a kind"]])
	pretty_card.add_row(["Full House", card["Full house"]])
	pretty_card.add_row(["Small straight", card["Small straight"]])
	pretty_card.add_row(["Large straight", card["Large straight"]])
	pretty_card.add_row(["YAHTZEE", card["Yahtzee"]])
	pretty_card.add_row(["YAHTZEE BONUS", card["Yahtzee bonus"]])
	pretty_card.add_row(["TOTAL SCORE", "--"])
	
	
	
	def addscore(self, category, score):
		if self.card[category] != None:
			print "You already scored %s" % category
		else:
			self.card[category] = score
			print "You scored %r for %s" % (score, category)
		

def category(choice):
	if choice == "ones":
		player1.addscore("Ones", scoring.digs(dice, 1))
		print player1.card
		
	elif choice == "twos":
		player1.addscore("Twos", scoring.digs(dice, 2))
		print player1.card
		
	elif choice == "threes":
		player1.addscore("Threes", scoring.digs(dice, 3))
		print player1.card

	elif choice == "fours":
		player1.addscore("Fours", scoring.digs(dice, 4))
		print player1.card

	elif choice == "fives":
		score = digs(dice, 5)
		print "Score is %r" % score
		
	elif choice == "sixes":
		score = digs(dice, 6)
		print "Score is %r" % score
		
	elif choice == "3k":
		score = threek(dice)
		print "Score is %r" % score
		
	elif choice == "4k":
		score = fourk(dice)
		print "Score is %r" % score
		
	elif choice == "fullhouse":
		score = fullhouse(dice)
		print "Score is %r" % score
		
	elif choice == "smlstrt":
		score = smlstrt(dice)
		print "Score is %r" % score
		
	elif choice == "lrgstrt":
		score = lrgstrt(dice)
		print "Score is %r" % score
		
	elif choice == "yahtzee":
		score = yahtzee(dice)
		print "Score is %r" % score

	elif choice == "chance":
		score = chance(dice)
		print "Score is %r" % score
		
	else:
		print "What?"
	
	
## main
print "Player 1 name?"
player1 = Score(raw_input("> "))


raw_input("Press ENTER to roll...")
dice = Dice()
dice.first_roll()
	




##User input testing
print "\nTest category?"
category(raw_input("> "))
