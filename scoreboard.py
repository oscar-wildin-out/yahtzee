def scoreboard(scores_dictionary, upper_score,total_score):

    print '---------------------------------------'
    print "Hand           | Points"
    print '---------------------------------------'
    print "Ones           | "+str(scores_dictionary[0])
    print "Twos           | "+str(scores_dictionary[1])
    print "Threes         | "+str(scores_dictionary[2])
    print "Fours          | "+str(scores_dictionary[3])
    print "Fives          | "+str(scores_dictionary[4])
    print "Sixes          | "+str(scores_dictionary[5])
    print '---------------------------------------'
    print "Upper total    | "+str(upper_score)
    print '---------------------------------------'
    print "3 of a kind    | "+str(scores_dictionary[6])
    print "4 of a kind    | "+str(scores_dictionary[7])
    print "Full house     | "+str(scores_dictionary[8])
    print "Small straight | "+str(scores_dictionary[9])
    print "Large straight | "+str(scores_dictionary[10])
    print "Yahtzee        | "+str(scores_dictionary[11])
    print "Chance         | "+str(scores_dictionary[12])
    print '---------------------------------------'
    print "Total          | "+str(total_score)
