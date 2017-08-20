import random

class Die(object):
    def roll(self):
        return random.randint(1, 6)

d = Die()

def keeper():
    keeper = raw_input("Which dice (numbered 1-5) would you like to keep? ")
    if keeper.lower() == "all":
        result = [1,2,3,4,5]
    elif len(keeper) == 0:
        result = 0
    else:
        keeper_list = keeper.split(',')
        result = map(int,keeper_list)
    return result

def New_Roll(previous_roll, keepers):
    kept_dice = []

    if keepers == 0: #if keepers is one value, it is type int
        kept_dice = [previous_roll[keepers-1]] #add the die we're keeping to kept_dice
        number_of_kept_dice = 1
    else:
        keepers[:] = [x - 1 for x in keepers] # ':' is the slicing operator, found this code online
        number_of_kept_dice = len(keepers)
        for dice in keepers:
            kept_dice.append(previous_roll[dice]) # add all the kept dice
        kept_dice.sort()

    if keepers == 0:
        print '---------------------------------------'
        print("Ok, we'll re-roll all the dice")
    else:
        print '---------------------------------------'
        print("Ok, we'll keep %s dice" % number_of_kept_dice)
    print("Now we'll roll the remaining dice again")

    for x in range(5 - number_of_kept_dice):
        kept_dice.append(d.roll())

    print '---------------------------------------'
    print("Here are your new dice: %s" % kept_dice)
    return kept_dice
