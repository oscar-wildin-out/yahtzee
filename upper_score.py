def upper_score(number, dice_counts):
    score = number * dice_counts[number-1]
    return score

print upper_score(3+1,[4, 0, 0, 4, 0, 0])
