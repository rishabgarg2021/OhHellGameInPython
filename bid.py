def bid(hand, player_no, phase_no, deck_top, reshuffled=False, 
        player_data=None, suppress_player_data=True):
    try:
        from collections import defaultdict as dd
        total=0
        deck_suit=deck_top[1]

        facecard=["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", 
                  "A"]
        tally1=dd(int)
        j=2
        list5=[]
        list6=[]
        for i in facecard:  #makes dictionary with rank of facecards
            tally1[i]=j
            j+=1

        for each_element in hand:
            total+=1
        if phase_no==1 or phase_no==19:
            list1=[]
            list2=[]
            bid=1
            for each_card in hand:
                list1.append(each_card[0])
                list2.append(each_card[1])
            #when one suit matches of any player bid is set to zero.
            for a in list2:
                if a==deck_suit:
                    bid=0
                    return bid
            #when suit doesnt match and needs to check their high card
            if bid==1:  #means no one has decks trump crd
                next_ls=hand[0][1]
                if player_no!=0:  #if we are at not at position 0 then nexxt 
                    #leadins suit wil be decided by zeroth player
                    for d in hand: 
                        if d[1] ==next_ls:
                            list5.append(tally1[d[0]])
                        else:
                            list6.append(d)
                    for e in list5:
                        if e>6:
                            bid=0
                            return bid
                    if bid==1:
                        return bid
                else:   #if we are at first position our suit will be laeding
                    #suit. our bid should be 1 as risk.
                    return bid
        if phase_no==4 or phase_no==8 or phase_no==12 or phase_no==16:
            bid=int(total/4)
            return bid
        elif phase_no==10:
            bid=0
            return bid
        elif phase_no==9 or phase_no==10:
            from collections import defaultdict as dd
            tally=dd(list)
            bid=0
            list4=[]
            deck_ls=deck_top[1]
            for e_card in hand:
                list4.append(e_card[0])
                #dictionary of our suits with its number
                tally[e_card[1]]+=list4 
                list4=[]
            if player_no==0:
                bid=0
                list5=[]
                for e_value in tally[deck_ls]:
                    list5.append(tally1[e_value])
                for b in list5:
                    if b>=8:
                        bid+=1
                del tally[deck_ls]
                for a, b in tally.items():
                    list9=[]
                    for c in b:
                        list9.append(tally1[c])
                    for number in list9:
                        if number>10:
                            bid+=1
                return bid
            else:
                bid=0
                list5=[]
                for e_value in tally[deck_ls]:
                    list5.append(tally1[e_value])
                for b in list5:
                    if b>=10:
                        bid+=1
                return bid
        else:
            from collections import defaultdict as dd
            tally=dd(list)
            bid=0
            list4=[]
            deck_ls=deck_top[1]
            for e_card in hand:
                list4.append(e_card[0])
                #dictionary of our suits with its number
                tally[e_card[1]]+=list4
                list4=[]
            if player_no==0:
                bid=0
                list5=[]
                for e_value in tally[deck_ls]:
                    list5.append(tally1[e_value])
                for b in list5:
                    if b>=10:
                        bid+=1
                del tally[deck_ls]
                for a, b in tally.items():
                    list9=[]
                    for c in b:
                        list9.append(tally1[c])
                    for number in list9:
                        if number>11:
                            bid+=1
                return bid
            else:
                bid=0
                list5=[]
                for e_value in tally[deck_ls]:
                    list5.append(tally1[e_value])
                for b in list5:
                    if b>=10:
                        bid+=1
                return bid
    except:
        bid=0
        return bid

      
        
        
            
            
            