from scoring_options import

def scoring(score_choice_value):
    if score_choice_value > 5:
        lower_scores = [0,0,0,0,0,0, sum(Third_Roll), sum(Third_Roll), 25, 30, 45, 50, sum(Third_Roll)]
    else:
        lower_scores = [upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count),
        upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count),
        upper_score(score_choice_value+1, dice_count), upper_score(score_choice_value+1, dice_count)]
        
    result = [lower_scores[score_choice_value], score_choice_value]
    return result
