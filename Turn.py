import random
import time
#from full_house import full_house
from dice_counts import dice_counts
from scoring_options import *
from roll import *
from score_choice import score_choice

class Die(object):
    def roll(self):
        return random.randint(1, 6)

def Turn(player_1_scores):

    d = Die()
    First_Roll = [d.roll(), d.roll(), d.roll(), d.roll(), d.roll()]

    print(First_Roll)

    First_Keepers = keeper()
    #input("Which dice (numbered 1-5) would you like to keep? ")
    Second_Roll = New_Roll(First_Roll, First_Keepers)

    Second_Keepers = keeper()
    Third_Roll = New_Roll(Second_Roll, Second_Keepers)

    dice_count = dice_counts(Third_Roll)

    score_array = lower_scoring_options(dice_count, player_1_scores)

    score_choice_values = score_choice()
    score_choice_value = score_choice_values[0]
    score_choice_word = score_choice_values[1]

    while player_1_scores[score_choice_value] == 1:# or score_array[score_choice_value] == 0:
        print "You've already used " + score_choice_word
        score_choice_values = score_choice()
        score_choice_value = score_choice_values[0]
        score_choice_word = score_choice_values[1]

    result = scoring(score_choice_value, dice_count, Third_Roll, score_array, score_choice_word)

    print "Your score for this turn is " + str(result[0])

    return result
