import random
import scoring
from dice import Dice
from prettytable import PrettyTable

## Score card class to be used for multiple players
class Score(object):

	def __init__(self, name, score = 0):
		self.name = name
		self.score = score
		self.card = {"Ones" : None,
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
		self.round = 0

	def card_gen(self):
		pretty_card = PrettyTable(["Category", self.name])
		pretty_card.add_row(["Ones", self.card["Ones"]])
		pretty_card.add_row(["Twos", self.card["Twos"]])
		pretty_card.add_row(["Threes", self.card["Threes"]])
		pretty_card.add_row(["Fours", self.card["Fours"]])
		pretty_card.add_row(["Fives", self.card["Fives"]])
		pretty_card.add_row(["Sixes", self.card["Sixes"]])
		pretty_card.add_row(["Bonus", self.card["Bonus"]])
		pretty_card.add_row(["------------", "-"])
		pretty_card.add_row(["3 of a kind", self.card["Three of a kind"]])
		pretty_card.add_row(["4 of a kind", self.card["Four of a kind"]])
		pretty_card.add_row(["Full House", self.card["Full house"]])
		pretty_card.add_row(["Small straight", self.card["Small straight"]])
		pretty_card.add_row(["Large straight", self.card["Large straight"]])
		pretty_card.add_row(["YAHTZEE", self.card["Yahtzee"]])
		pretty_card.add_row(["Chance", self.card["Chance"]])
		pretty_card.add_row(["YAHTZEE BONUS", self.card["Yahtzee bonus"]])
		pretty_card.add_row(["TOTAL SCORE", "--"])
		print pretty_card

	def addscore(self, category, score, dice):
		while True:
			if category == "Yahtzee bonus":
				if self.card[category] == None:
					self.card[category] = 100
					print "You got another Yahtzee! You scored 100 bonus points!"
					break
				self.card[category] += score
				break
			elif self.card[category] == None:
				self.card[category] = score
				print "You scored %r for %s!\n" % (score, category)
				break
			print "You already scored %s, please pick an empty category.\n" % category
			print dice
			self.cat_choice(dice)
			break

	def cat_choice(self, dice):
		while True:
			choice = raw_input("What category would you like to score for?\n> ")
			if choice == "ones":
				self.addscore("Ones", scoring.digs(dice, 1), dice)
				self.card_gen()
				break

			elif choice == "twos":
				self.addscore("Twos", scoring.digs(dice, 2), dice)
				self.card_gen()
				break

			elif choice == "threes":
				self.addscore("Threes", scoring.digs(dice, 3), dice)
				self.card_gen()
				break

			elif choice == "fours":
				self.addscore("Fours", scoring.digs(dice, 4), dice)
				self.card_gen()
				break

			elif choice == "fives":
				self.addscore("Fives", scoring.digs(dice, 5), dice)
				self.card_gen()
				break

			elif choice == "sixes":
				self.addscore("Sixes", scoring.digs(dice, 6), dice)
				self.card_gen()
				break

			elif choice == "3k":
				self.addscore("Three of a kind", scoring.threek(dice), dice)
				self.card_gen()
				break

			elif choice == "4k":
				self.addscore("Four of a kind", scoring.fourk(dice), dice)
				self.card_gen()
				break

			elif choice == "fullhouse":
				self.addscore("Full house", scoring.fullhouse(dice), dice)
				self.card_gen()
				break

			elif choice == "smlstrt":
				self.addscore("Small straight", scoring.smlstrt(dice), dice)
				self.card_gen()
				break

			elif choice == "lrgstrt":
				self.addscore("Large straight", scoring.lrgstrt(dice), dice)
				self.card_gen()
				break

			elif choice == "yahtzee":
				if self.card["Yahtzee"] > 0:
					self.addscore("Yahtzee bonus", 100, dice)
				else:
					self.addscore("Yahtzee", scoring.yahtzee(dice), dice)
				self.card_gen()
				break

			elif choice == "chance":
				self.addscore("Chance", scoring.chance(dice), dice)
				self.card_gen()
				break

			print "Please type a valid score category...\n"

	def end_game(self):
		if self.card["Ones"] + self.card["Twos"] + self.card["Threes"] + self.card["Fours"] + self.card["Fives"] + self.card["Sixes"] >= 63:
			self.card["Bonus"] = 35
			print "You scored a bonus 35 points for upper section!"
		else:
			self.card["Bonus"] = 0
		if self.card["Yahtzee bonus"] == None:
			self.card["Yahtzee bonus"] = 0
		total = sum(self.card.itervalues())
		print "%s, your total score was: %r" % (self.name, total)

def round(player):
	print "\nYour turn, %s." % player.name
	dice = Dice()
	roll1 = dice.first_roll()
	roll2 = dice.second_roll(roll1)
	roll3 = dice.third_roll(roll2)
	player.cat_choice(roll3)
	player.round += 1

def winner():
	p1 = sum(player1.card.itervalues())
	p2 = sum(player2.card.itervalues())
	if p1 > p2:
		print "\n--------------------------"
		print "\n       ~*- %s wins!!! -*~" % player1.name
		print "\n--------------------------"
	elif p2 > p1:
		print "\n--------------------------"
		print "\n       ~*- %s wins!!! -*~" % player2.name
		print "\n--------------------------"
	else:
		print "\nThe game was a tie! Wow!"

print "----------------------------------------------"
print "\n\n\n          ~*- WELCOME TO TEXT YAHTZEE -*~"
print "\n           created in Python by Shane!\n\n"
print "----------------------------------------------\n"

playercount = raw_input("One or Two Players?\n> ")

if playercount == 2 or "two" in str(playercount.lower()):
	player1 = Score(raw_input("Player 1 Name?\n> "))
	player2 = Score(raw_input("Player 2 Name?\n> "))
else:
	player1 = Score(raw_input("Player name?\n> "))

while player1.round < 13:
	round(player1)
	if player1.round == 13:
		player1.end_game()
	try:
		if player2:
			round(player2)
		if player2.round == 13:
			player2.end_game()
	except NameError:
		pass
while True:
	try:
		winner()
		break
	except NameError:
		pass
