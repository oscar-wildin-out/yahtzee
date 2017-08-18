def keeper():
    keeper = raw_input("Which dice (numbered 1-5) would you like to keep? ")

    if keeper.lower() == "all":
        result = [1,2,3,4,5]
    elif len(keeper) == 0:
        result = 0
    else:
        keeper_list = keeper.split(',')
        result = map(int,keeper_list)

    print result
    print type(result)
    return result

keeper()
