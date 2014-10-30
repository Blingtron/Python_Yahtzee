from dice import Dice
import scoring



dice = Dice()

roll1 = dice.first_roll()
roll2 = dice.second_roll(roll1)
roll3 = dice.third_roll(roll2)