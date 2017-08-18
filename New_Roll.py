import random

class Die(object):
    def roll(self):
        return random.randint(1, 6)

d = Die()

def keeper():
    keeper = raw_input("Which dice (numbered 1-5) would you like to keep? ")
    if len(keeper) == 0:
        result = 0
    else:
        keeper_list = keeper.split(',')
        keeper_array = map(int,keeper_list)
        result = tuple(keeper_array)
    return result

def New_Roll(previous_roll, keepers):
    kept_dice = []
    if type(keepers) == int: #if keepers is one value, it is type int
        kept_dice = [previous_roll[keepers-1]] #add the die we're keeping to kept_dice
        number_of_kept_dice = 1
    else:
        keepers = list(keepers) #convert tuple to list
        keepers[:] = [x - 1 for x in keepers] # ':' is the slicing operator, found this code online
        number_of_kept_dice = len(keepers)
        for dice in keepers:
            kept_dice.append(previous_roll[dice]) # add all the kept dice

    if number_of_kept_dice == 1:
        print '---------------------------------------'
        print("Alright, we'll keep 1 die")
    else:
        print '---------------------------------------'
        print("Alright, we'll keep "+str(number_of_kept_dice)+" dice")
    print("Now we'll roll the remaining dice again")

    for x in range(5 - number_of_kept_dice):
        kept_dice.append(d.roll())

    print '---------------------------------------'
    print("Here are your new dice: " + str(kept_dice))
    return kept_dice
