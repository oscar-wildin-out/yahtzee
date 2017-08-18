import random
import time
#from full_house import full_house
from dice_counts import dice_counts
from scoring_options import lower_scoring_options
from New_Roll import New_Roll
from Turn import Turn
from scoreboard import scoreboard

total_score = 0
upper_score = 0

global player_1_scores
player_1_scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores_dictionary = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

while 0 in player_1_scores:
    round_result = Turn(player_1_scores)
    total_score += round_result[0]
    if round_result[1] < 6:
        upper_score += round_result[0]
    player_1_scores[round_result[1]] = 1
    if round_result[0] == 0:
        scores_dictionary[round_result[1]] = "Used"
    else: scores_dictionary[round_result[1]] = round_result[0]
    #print "Your score is: " + str(total_score)
    scoreboard_check = raw_input("Would you like to check your scoreboard? ")
    if scoreboard_check.lower() == "yes":
        scoreboard(scores_dictionary,upper_score,total_score)
    print '---------------------------------------'

print "Your upper score was: " + str(upper_score)

if upper_score >= 63:
    print "Since your upper score of "+str(upper_score)+" was greater than 63, you receive 35 bonus points!"
    total_score += 35
elif upper_score < 63: "Since you didn't score 63 or over you do not qualify for the bonus"

print "Your grand total is " + str(total_score)
