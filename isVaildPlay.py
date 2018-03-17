def is_valid_play(play, curr_trick, hand):
    #checks if potential card is in hand and is valid
    if play in hand:
        #if we have empty curr_trick, our potential card is always valid
        if not curr_trick:
            return True
        else:
            for a in hand:
                #return False if we dont throw any card which we have of the
                # suit as curreent cards first card by check each card in hand
                #through for loop.
                if a[1]==curr_trick[0][1] and a[1]!=play[1]:
                    return False
            return True
    else:
        return False