import random
import scoring
from dice import Dice
from prettytable import PrettyTable

## Score card class to be used for multiple players
class Score(object):

	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	round = 0

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



	def addscore(self, category, score, dice):
		while True:
			if self.card[category] == None:
				self.card[category] = score
				print "You scored %r for %s!\n" % (score, category)
				break
			print "You already scored %s, please pick an empty category.\n" % category
			print dice
			cat_choice(dice)
			break

	def end_game(self):
		if self.card["Ones"] + self.card["Twos"] + self.card["Threes"] + self.card["Fours"] + self.card["Fives"] + self.card["Sixes"] >= 63:
			self.card["Bonus"] = 35
			print "You scored a bonus 35 points for upper section!"
		else:
			self.card["Bonus"] = 0
		if self.card["Yahtzee bonus"] == None:
			self.card["Yahtzee bonus"] = 0
		total = sum(self.card.itervalues())
		print "Your total score was: ", total


def cat_choice(dice):
	while True:
		choice = raw_input("What category would you like to score for?\n> ")
		if choice == "ones":
			player1.addscore("Ones", scoring.digs(dice, 1), dice)
			print player1.card
			break

		elif choice == "twos":
			player1.addscore("Twos", scoring.digs(dice, 2), dice)
			print player1.card
			break

		elif choice == "threes":
			player1.addscore("Threes", scoring.digs(dice, 3), dice)
			print player1.card
			break

		elif choice == "fours":
			player1.addscore("Fours", scoring.digs(dice, 4), dice)
			print player1.card
			break

		elif choice == "fives":
			player1.addscore("Fives", scoring.digs(dice, 5), dice)
			print player1.card
			break

		elif choice == "sixes":
			player1.addscore("Sixes", scoring.digs(dice, 6), dice)
			print player1.card
			break

		elif choice == "3k":
			player1.addscore("Three of a kind", scoring.threek(dice), dice)
			print player1.card
			break

		elif choice == "4k":
			player1.addscore("Four of a kind", scoring.fourk(dice), dice)
			print player1.card
			break

		elif choice == "fullhouse":
			player1.addscore("Full house", scoring.fullhouse(dice), dice)
			print player1.card
			break

		elif choice == "smlstrt":
			player1.addscore("Small straight", scoring.smlstrt(dice), dice)
			print player1.card
			break

		elif choice == "lrgstrt":
			player1.addscore("Large straight", scoring.lrgstrt(dice), dice)
			print player1.card
			break

		elif choice == "yahtzee":
			player1.addscore("Yahtzee", scoring.yahtzee(dice), dice)
			print player1.card
			break

		elif choice == "chance":
			player1.addscore("Chance", scoring.chance(dice), dice)
			print player1.card
			break

		print "Please type a valid score category"



player1 = Score("name")

print "----------------------------------------------"
print "\n\n\n          ~*- WELCOME TO TEXT YAHTZEE -*~"
print "\n           created in Python by Shane!\n\n"
print "----------------------------------------------\n"

while player1.round < 13:
	dice = Dice()
	roll1 = dice.first_roll()
	roll2 = dice.second_roll(roll1)
	roll3 = dice.third_roll(roll2)
	cat_choice(roll3)
	player1.round += 1

player1.end_game()
