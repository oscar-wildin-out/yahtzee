import random
import time
#from full_house import full_house
from dice_counts import dice_counts
from scoring_options import lower_scoring_options
from New_Roll import New_Roll
from Turn import Turn
from scoreboard import scoreboard
import operator
#print "This is my multiple_yahtzees branch"

number_of_players = input("How many players are playing? ")
player_names = raw_input("Please enter the player names: ").split(', ')

while number_of_players != len(player_names):
    player_names = raw_input("Please enter %s player names: " % number_of_players).split(', ')
total_scores = dict()
upper_scores = dict()
player_scores = dict()
player_scores_dictionary = dict()
yahtzee_count = dict()
for i in player_names:
    total_scores[i] = 0 #holds a single value for each player which is their total score
    upper_scores[i] = 0 #holds a single value for each player which is their upper score
    player_scores[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #holds a list for each player which identifies if they've used a turn before or not
    player_scores_dictionary[i] = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0} #this is only used for printing the scoreboard
    yahtzee_count[i] = 0

for i in xrange(13):
    for name in player_names:
        format_line = '---------------------------------------'
        print format_line
        if len(player_names) > 1: #If only one player is playing, it is unnecessary to keep telling them it's their turn
            print "It is now %s\'s turn" % name

        if raw_input("Would you like to check your scoreboard? ").lower() ==  "yes":
            print format_line
            print "%s\'s Scoreboard:" % name
            scoreboard(player_scores_dictionary[name],upper_scores[name],total_scores[name])

        round_result = Turn(player_scores[name], player_scores_dictionary[name]) #Turn returns the score for the round and the 'hand' that they used
        score = round_result[0]
        hand = round_result[1]

        if hand < 6:
            upper_scores[name] += score #adds the score to the upper_score if applicable

        if hand == 11: #Yahtzees will be treated as a special case
            if score == 0:
                player_scores_dictionary[name][11] = "Used"
            elif player_scores[name][hand] == 0:
                player_scores[name][11] += 1
                player_scores_dictionary[name][11] = "50"
                total_scores[name] += 50
                score = 50
            else:
                player_scores[name][11] +=1
                player_scores_dictionary[name][11] += ", 100"
                total_scores[name] += 100
                score = 100
        else:
            player_scores[name][hand] = 1 #Checks off that this hand has been used in the player_scores list
            if score == 0:
                player_scores_dictionary[name][hand] = "Used"
            else: player_scores_dictionary[name][hand] = score
            total_scores[name] += score
        print "Your score for this turn is %s" % score

for name in player_names:
    print format_line
    print name+", your upper score was %s" % upper_scores[name]
    if upper_scores[name] >= 63:
        print "Since your upper score of %s was greater than 63, you receive 35 bonus points!" % upper_scores[name]
        total_scores[name] += 35
    elif upper_scores[name] < 63: print "Since you didn't score 63 or over you do not qualify for the bonus"
    print "Your grand total is %s" % total_scores[name]

print format_line
winner = max(total_scores.iteritems(), key=operator.itemgetter(1))[0]
print "The winner is %s, with a score of %s" % (winner, total_scores[winner])
