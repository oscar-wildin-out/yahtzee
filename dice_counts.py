def dice_counts(dice):
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0

    for i in range(0,5):
        if dice[i] == 1:
            one_count += 1
        elif dice[i] == 2:
            two_count += 1
        elif dice[i] == 3:
            three_count += 1
        elif dice[i] == 4:
            four_count += 1
        elif dice[i] == 5:
            five_count += 1
        elif dice[i] == 6:
            six_count += 1

    dice_count_list = [one_count, two_count, three_count, four_count, five_count, six_count]

    return dice_count_list
