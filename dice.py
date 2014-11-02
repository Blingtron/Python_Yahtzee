import random

class Dice():


	def dice(self, num):
		dice = []
		for i in range(num):
			dice.append(random.randint(1,6))
		return dice

	def first_roll(self):
		raw_input("Press ENTER to roll the dice...")
		roll1 = self.dice(5)
		return roll1

	def second_roll(self, roll1):
		print roll1
		print "Which dice would you like to keep? [0,4]"
		keep_index = raw_input("> ")
		# creates a list by mapping input "x x x x x" as integers
		# to [x, x, x, x, x]
		keep_index = map(int, keep_index.split())

		keep_dice = []
		roll2 = self.dice(5 - len(keep_index))

		for i in keep_index:
			keep_dice.append(roll1[i])


		print "You kept dice: ", keep_dice
		raw_input("\nPress ENTER to roll the other dice...\n")
		print "You rolled: ", roll2
		keep_dice = keep_dice + roll2
		print "\nYour dice are: ", keep_dice
		return keep_dice

	def third_roll(self, roll2):
		print "\nWhich dice would you like to keep? [0, 4]"
		keep_index = raw_input("> ")
		keep_index = map(int, keep_index.split())

		keep_dice = []
		roll3 = self.dice(5 - len(keep_index))

		for i in keep_index:
			keep_dice.append(roll2[i])
		print "You kept dice: ", keep_dice
		raw_input("\nPress ENTER to roll the other dice...\n")
		keep_dice = keep_dice + roll3
		print "\nYour dice are: ", keep_dice
		return keep_dice
