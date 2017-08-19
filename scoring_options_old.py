def lower_scoring_options(dice_counts, player_1_scores):
    lower_score_array = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]

    if 3 in dice_counts or 4 in dice_counts or 5 in dice_counts:
        lower_score_array[6] = 1 #3 of a kind

    if 4 in dice_counts or 5 in dice_counts:
        lower_score_array[7] = 1 #print 4 of a kind

    if 3 in dice_counts and 2 in dice_counts:
        lower_score_array[8] = 1 #Full House

    if (dice_counts == [1, 1, 1, 1, 1, 0] or dice_counts == [1, 0, 1, 1, 1, 1]  or dice_counts == [1, 1, 1, 1, 0, 1]
    or dice_counts == [1, 1, 1, 2, 0, 0] or dice_counts == [1, 1, 2, 1, 0, 0] or dice_counts == [1, 2, 1, 1, 0, 0]
    or dice_counts == [2, 1, 1, 1, 0, 0] or dice_counts == [0, 1, 1, 1, 1, 1] or dice_counts == [0, 0, 1, 1, 1, 2]
    or dice_counts == [0, 0, 1, 1, 2, 1] or dice_counts == [0, 0, 1, 2, 1, 1] or dice_counts == [0, 0, 2, 1, 1, 1]
    or dice_counts == [0, 2, 1, 1, 1, 0] or dice_counts == [0, 1, 2, 1, 1, 0] or dice_counts == [0, 1, 1, 2, 1, 0]
    or dice_counts == [0, 1, 1, 1, 2, 0]
    ) :
        lower_score_array[9] = 1 #Small straight

    if dice_counts == [1, 1, 1, 1, 1, 0] or dice_counts == [0, 1, 1, 1, 1, 1]:
        lower_score_array[10] = 1 #Large Straight

    if 5 in dice_counts:
        lower_score_array[11] = 1 #Yahtzee

    return lower_score_array

def upper_score(number, dice_counts):
    score = number * dice_counts[number-1]
    return score


def scoring(score_choice_value, dice_count, roll, score_array, score_choice_word):
    if score_choice_value > 5:
        scores = [0,0,0,0,0,0, sum(roll), sum(roll), 25, 30, 40, 50, sum(roll)]
        if score_array[score_choice_value] == 0:
            print "Since you have not rolled a " + score_choice_word + " you'll receive no points for this turn"
            result = [0, score_choice_value]
        else: result = [scores[score_choice_value], score_choice_value]
    else:
        scores = [upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count),
        upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count),
        upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count)]
        result = [scores[score_choice_value], score_choice_value]
    return result
