import random
import time
#from full_house import full_house
from dice_counts import dice_counts
from scoring_options import lower_scoring_options
from New_Roll import New_Roll
from Turn import Turn
from scoreboard import scoreboard
import operator

number_of_players = input("How many players are playing? ")
player_names = raw_input("Please enter the player names: ").split(', ')
while number_of_players != len(player_names):
    player_names = raw_input("Please enter "+str(number_of_players)+" player names: ").split(', ')
total_scores = dict()
upper_scores = dict()
player_scores = dict()
player_scores_dictionary = dict()
for i in player_names:
    total_scores[i] = 0 #holds a single value for each player which is their total score
    upper_scores[i] = 0 #holds a single value for each player which is their upper score
    player_scores[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #holds a list for each player which identifies if they've used a turn before or not
    player_scores_dictionary[i] = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

for i in xrange(13):
    for name in player_names:
        print '---------------------------------------'
        print "It is now "+name+"\'s turn"
        scoreboard_check = raw_input("Would you like to check your scoreboard? ")
        if scoreboard_check.lower() == "yes":
            print '---------------------------------------'
            print name+"\'s Scoreboard:"
            scoreboard(player_scores_dictionary[name],upper_scores[name],total_scores[name])

        round_result = Turn(player_scores[name], player_scores_dictionary[name]) #Turn returns the score for the round and the 'hand' that they used
        total_scores[name] += round_result[0]

        if round_result[1] < 6:
            upper_scores[name] += round_result[0] #adds the score to the upper_score if applicable

        player_scores[name][round_result[1]] = 1 #Checks off that this hand has been used in the player_scores list

        if round_result[0] == 0:
            player_scores_dictionary[name][round_result[1]] = "Used"
        else: player_scores_dictionary[name][round_result[1]] = round_result[0]

for name in player_names:
    print '---------------------------------------'
    print name+", your upper score was " + str(upper_scores[name])
    if upper_scores[name] >= 63:
        print "Since your upper score of "+str(upper_scores[name])+" was greater than 63, you receive 35 bonus points!"
        total_scores[name] += 35
    elif upper_scores[name] < 63: print "Since you didn't score 63 or over you do not qualify for the bonus"
    print "Your grand total is " + str(total_scores[name])

print '---------------------------------------'
winner = max(total_scores.iteritems(), key=operator.itemgetter(1))[0]
print "The winner is "+winner+", with a score of "+str(total_scores[winner])
