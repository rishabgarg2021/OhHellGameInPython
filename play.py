def bid(hand, player_no, phase_no, deck_top, reshuffled=False, player_data=None, suppress_player_data=True):
    from collections import defaultdict as dd
    dd1=dd(list)
    total=0
    deck_suit=deck_top[1]
    
    facecard=["2","3","4","5","6","7","8","9","0","J","Q","K","A"]
    tally1=dd(int)
    j=2
    tally3=dd(list)
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
        if bid==1: #means no one has decks trump crd
          
            next_ls=hand[0][1]
            next_ln=tally1[hand[0][0]]
            if player_no!=0:#if we are at not at position 0 then nexxt leadins suit wil be decided by zeroth player
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
            else: #if we are at first position our suit will be laeding suit. our bid should be 1 as risk.
                return bid
                
                
                
                
            
            
            
        
    elif phase_no==4 or phase_no==8 or phase_no==12 or phase_no==16:
        
        bid=int(total/4)
        return bid
        
    elif phase_no==10:
        bid=0
        return bid
    elif phase_no==9 or phase_no==11:
        from collections import defaultdict as dd
        tally=dd(list)
        bid=0
        list4=[]
        deck_ls=deck_top[1]
        for e_card in hand:
        
            list4.append( e_card[0])
            tally[e_card[1]]+=list4 #dictionary of our suits with its number
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
            
            for a,b in tally.items():
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
            print(list5)
            for b in list5:
                if b>=8:
                    bid+=1
            return bid
    else:
        from collections import defaultdict as dd
        tally=dd(list)
        bid=0
        list4=[]
        deck_ls=deck_top[1]
        for e_card in hand:
        
            list4.append( e_card[0])
            tally[e_card[1]]+=list4 #dictionary of our suits with its number
            list4=[]
        if player_no==0:
            bid=0
            
                
            list5=[]
            for e_value in tally[deck_ls]:
                list5.append(tally1[e_value])
            print(list5)
            for b in list5:
                if b>=10:
                    bid+=1
            del tally[deck_ls]
            
            for a,b in tally.items():
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


def score_phase(bids, tricks, deck_top, player_data=None, suppress_player_data=True):
    from collections import defaultdict as dd
    # Implement this function.
    facecard=["2","3","4","5","6","7","8","9","0","J","Q","K","A"]
    tally1=dd(int)
    tally2={0:0,1:0,2:0,3:0}
    j=2
    for i in facecard:  #makes dictionary with rank of facecards
        tally1[i]=j
        j+=1

    dd=dd(list)
    i=0
    order=[0,1,2,3]
    list1=[]
    list2=[]
    tally={}
    for trick in tricks[:]:   #list1 is the list of all cards in phase with position
       
        
        
        for j in trick:
            list1.append((order[i],j))
            i=i+1
        
        
    #makes dictionary tally which gives the bigram dictionary of each suit with position and card with each player.
        for d in list1:
            if d[1][1] in tally:
                list2.append(d)
            
                tally[d[1][1]]+=list2
                list2 = []
            else:
                tally[d[1][1]]=[d]
    
        
        list4=[]
    #list4 is composed of all players position whos holding trump card
        for a,b in tally.items():
        #checks if it has that suit's deck card
            if a == deck_top[1]:
                list4.append(b)
        if list4!=[]:
       
            list5=[]
        #makes new list with position of player and that that decks matching card rank comparedd to tallly1.
            for y in list4:
                for z in y:
                    list5.append((tally1[z[1][0]],z[0]))
            list5=sorted(list5)
            pos_w=list5[-1][1] 
            
        #initialize every players point to zero and 1 if its winner of that particular round.
            for i in range(4):
                pos_w=list5[-1][1]
                if i == pos_w:
                    tally2[pos_w]+=1 
            #position with score
               
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            i=0
            if pos_w==1:
                order=[1,2,3,0]
            elif pos_w==2:
                order=[2,3,0,1]
            elif pos_w==3:
                order=[3,0,1,2]
            else :
                order=[0,1,2,3]
            tally={}
        else:
          
            list7=list(tally.values())
       
           
        # for loop determines the next leading suit of zeroth position
            new_suit=list1[0][1][1]
          
            list8=[]
        # gets cards with position of players which has that particular suit and  position.
            for a,b in tally.items():
                if a==new_suit:
                    list8.append(b)
        
            list9=[]
        #gets position of each player who has next leading suit and rank of theirr card
            for c in list8:
                for d,f in c:
         
                
                    list9.append((tally1[f[0]],d))
    
            list9=sorted(list9)
            
        #gets position of player who has next leading suit+ highest card of that particular suit
            pos_w=list9[-1][-1]
          
        #in same tally2 dictionary points are added of each player.
           
            for i in range(4):
                if i == pos_w:
                    tally2[pos_w]+=1 
            #position with score
                
         
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            list6=[]
            list7=[]
            list8=[]
            list9=[]
            i=0
            tally={}
            if pos_w==1:
                order=[1,2,3,0]
            elif pos_w==2:
                order=[2,3,0,1]
            elif pos_w==3:
                order=[3,0,1,2]
            else :
                order=[0,1,2,3]
             
   
    tally2=tally2.items()
  
    list10=[]
    i=0
    for a,b in tally2:
        
        if bids[i]==b:
            b=b+10
          
        i+=1
        list10.append((b)) 
    return tuple(list10)
        
        


def play(curr_trick, hand, prev_tricks, player_no, deck_top, phase_bids, player_data=None, suppress_player_data=True, is_valid=is_valid_play, score=score_phase):
    #just consedring (hand) (current trick) and (deck top).
    from collections import defaultdict as dd
    tally=dd(list)
    list1=[]
     #position of card in our hand
    
    #makes tally dictionary which gives cards in our hand of each and every suit with position of that in our hand
    facecard=["2","3","4","5","6","7","8","9","0","J","Q","K","A"]
    j=2
    tally4=dd(int)
    for i in facecard:  #makes dictionary with rank of facecards
        tally4[i]=j
        j+=1
   # print(tally4)
    for e_card in hand:
        
        list1.append( e_card[0])
        tally[e_card[1]]+=list1 #dictionary of our suits with its number
        list1=[]
        
   # print(tally)
    tally2=dd(list)
    list2=[]
    for e_card1 in curr_trick:
        list2.append(e_card1[0])
        tally2[e_card1[1]]+=list2
        list2=[]
  #  print(tally2)
    tally3=dd(list)
    list3=[]
    for e_card2 in prev_tricks:
        list3.append(e_card2[0])
        tally3[e_card2[1]]+=list3
        list3=[]
    #print(tally3)
   # o_bid=phase_bids[player_no]
   # print(o_bid)
    list_h=[]
    list_h1=[]
# print(tally4) #tally4 is dictionary of facecards with its value
    #checks if i have deck cards suit or not. and i want to win as my bid is not zero
    from collections import defaultdict as dd
    # Implement this function.
    facecard=["2","3","4","5","6","7","8","9","0","J","Q","K","A"]
    tally1=dd(int)
    taly2={0:0,1:0,2:0,3:0}
    j=2
    for i in facecard:  #makes dictionary with rank of facecards
        tally1[i]=j
        j+=1

    dd=dd(list)
    i=0
    order=[0,1,2,3]
    list1=[]
    list2=[]
    taly={}
    for trick in prev_tricks[:]:   #list1 is the list of all cards in phase with position
       
        
        
        for j in trick:
            list1.append((order[i],j))
            i=i+1
        
        
    #makes dictionary tally which gives the bigram dictionary of each suit with position and card with each player.
        for d in list1:
            if d[1][1] in taly:
                list2.append(d)
            
                taly[d[1][1]]+=list2
                list2 = []
            else:
                taly[d[1][1]]=[d]
    
        
        list4=[]
    #list4 is composed of all players position whos holding trump card
        for a,b in taly.items():
        #checks if it has that suit's deck card
            if a == deck_top[1]:
                list4.append(b)
        if list4!=[]:
       
            list5=[]
        #makes new list with position of player and that that decks matching card rank comparedd to tallly1.
            for y in list4:
                for z in y:
                    list5.append((tally1[z[1][0]],z[0]))
            list5=sorted(list5)
            pos_w=list5[-1][1] 
            
        #initialize every players point to zero and 1 if its winner of that particular round.
            for i in range(4):
                pos_w=list5[-1][1]
                if i == pos_w:
                    taly2[pos_w]+=1 
            #position with score
               
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            i=0
            if pos_w==1:
                order=[1,2,3,0]
            elif pos_w==2:
                order=[2,3,0,1]
            elif pos_w==3:
                order=[3,0,1,2]
            else :
                order=[0,1,2,3]
            taly={}
        else:
          
            list7=list(taly.values())
       
           
        # for loop determines the next leading suit of zeroth position
            new_suit=list1[0][1][1]
          
            list8=[]
        # gets cards with position of players which has that particular suit and  position.
            for a,b in taly.items():
                if a==new_suit:
                    list8.append(b)
        
            list9=[]
        #gets position of each player who has next leading suit and rank of theirr card
            for c in list8:
                for d,f in c:
         
                
                    list9.append((tally1[f[0]],d))
    
            list9=sorted(list9)
            
        #gets position of player who has next leading suit+ highest card of that particular suit
            pos_w=list9[-1][-1]
          
        #in same tally2 dictionary points are added of each player.
           
            for i in range(4):
                if i == pos_w:
                    taly2[pos_w]+=1 
            #position with score
                
         
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            list6=[]
            list7=[]
            list8=[]
            list9=[]
            i=0
            taly={}
            if pos_w==1:
                order=[1,2,3,0]
            elif pos_w==2:
                order=[2,3,0,1]
            elif pos_w==3:
                order=[3,0,1,2]
            else :
                order=[0,1,2,3]
                
    scores=score(phase_bids,prev_tricks,deck_top,player_data=None)
    
    player=0
    
    score_m=taly2[player_no]
    total=0
    player_no1=player_no
    for a in curr_trick:
        total+=1
    
    player_no=total  
   
    if phase_bids[player_no1]>score_m or phase_bids[player_no1]<score_m:              
        
        
        if deck_top[1] in tally.keys(): #if dcks trump card mathcs wth suit of ours
            if  curr_trick==() or curr_trick==[]:
               # print("tt")
                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))#gets list sorted in ascending order
               # print(sorted_list)
                
                return sorted_list[-1]
                
            elif deck_top[1] ==curr_trick[0][1]: #if decks trump card matches with current trick
               # print("r")
                tally2_value=tally2[deck_top[1]]
                #print(tally2_value)
                list7=[]
                for a in tally2_value:
                    list7.append(tally4[a]) #list 7 contains all elements in current trick
                 
                m_tally2=max(list7) #maximum value of decktop suit in current trick
                
                tally_value=tally[deck_top[1]]
                list8=[]
                for b in tally_value:
                    list8.append(tally4[b]) #list8 contains all elements of that trump suit
                    
                m_tally=max(list8)   #gives highest value of decks leading suit from our hand in m_tally
                #print(m_tally)     
                #print(m_tally2)#gives highest value of decks leading suit from current trick
                
                
                #maximum v3alue of decktop suit in hand
                #if we are at last position we will throw just next card of decks leading suit
                if player_no==3: #player no.3 is best to decide which card to throw
                    
                    list9=list8.copy()
                    list9=sorted(list9) #list9 contains everything sorted of values of trump card
                    
                    for element in list9: 
                        if element>m_tally2:  #gives list of that elements whos trump suit matches and 
                                               
                            list_h.append(element)
                           
                            for a,b in tally4.items():
                                if b==list_h[0]:
                                    lh=a    
                                   
                            
                        else:
                            list_h1.append(element)
                            
                            for a,b in tally4.items():
                                if b==list_h1[0]:
                                    lh1=a
                    if list_h!=[]:
                        return lh+deck_top[1]
                    else:
                        return lh1+deck_top[1]
                elif  player_no!=3 and player_no!=0:#if position is not 3 bu some other position  of player
                     #player no.3 is best to decide which card to throw
                    
                    list9=list8.copy()
                    list9=sorted(list9) #list9 contains everything sorted of value sof trump card
                    
                    for element in list9: 
                        if element>m_tally2:  #gives list of that elements whos trump suit matches 
                                               
                            list_h.append(element)
                            
                           
                           
                            for a,b in tally4.items(): #return highest card of that suit
                                if b==list_h[-1] :
                                    lh=a
                                    
                            
                        else:
                            list_h1.append(element)
                            
                            for a,b in tally4.items():
                                if b==list_h1[0]:
                                    lh1=a
                    if list_h!=[]:
                        return lh+deck_top[1]
                    else:
                        return lh1+deck_top[1]
                                    
                else:#if player position is 0 current trick is empty
                    return m_tally+deck_top[1]
                
                    
                    
            
            else: #if next_leadingsuit is occuring
                #print("rr")
               # print(player_no)#if decks trump card is not with us .
                if  curr_trick==() or curr_trick==[]:
               # print("tt")
                    #gets list sorted in ascending order#COMEBACK
               # print(sorted_list)
                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                    list1=[]
                    for a in sorted_list:
                        tally_value=tally4[a[0]]
                        list1.append((tally_value,a[-1]))
                    list1=sorted(list1)
                    for a,b in tally4.items():
                        if b==list1[0][0]:
                            return a+list1[0][1]
                    
                elif player_no!=0:
                 #   print("r")
                    next_ls=curr_trick[0][1]    #next leading suit of current tricks suit because we dont have that suit  
                    #print(next_ls)
                  #  print(curr_trick[0][1])
                    if next_ls==deck_top[1]:
                       # print("t")#we need to throw card of lowest suit.
                        if deck_top[1] in tally2.keys(): #if decks trump card matches with current trick


                            #gets list sorted in ascending order

                            sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                            list1=[]
                            for a in sorted_list:
                                tally_value=tally4[a[0]]
                                list1.append((tally_value,a[-1]))
                            list1=sorted(list1)
                            for a,b in tally4.items():
                                if b==list1[0][0]:
                                    return a+list1[0][1]
                    else: #if next leading suit is not same as decks trump card
                        #we need to throw card of next leading suit first than other. least 
                        #else throw ur max of next leading suit
                       # print("o")
                        list11=[]
                        if  next_ls==tally.keys():
                            if deck_top[1]in tally.keys():
                                
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11)
                                    for a,b in tally4.items():
                                        if b==list11[0]:
                                            return a+next_ls
                                else:
                                    tally_values=tally[deck_top[1]]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11)
                                    for a,b in tally4.items():
                                        if b==list11[-1]:
                                            return a+next_ls
                            
                        else:#we have next leading suit but dont have trump card
                            list13=[]
                            
                            for a in curr_trick:
                                list13.append(a[1])
                           # print(list13)
                            if deck_top[1] in list13:#if we have deck_top in current trick and we dont have that trump card we will throw smallest next_leading card else throw highest next leading card
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11)
                                    for a,b in tally4.items():
                                        if b==list11[0]:
                                            return a+next_ls
                                else:
                                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))
                                            
                                    list1=[]
                                    for a in sorted_list:
                                        tally_value=tally4[a[0]]
                                        list1.append((tally_value,a[-1]))
                                    list1=sorted(list1)
                                    for a,b in tally4.items():
                                        if b==list1[0][0]:
                                            return a+list1[0][1]
                            else:# have  trump card in current_trick . next_ls we need to throw and compared to current we need to throw
                              
#  print("rrrrrrrrrrrrr")





                                
                                list11=[]
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11) #our values sortted of next_ls
                                    #we need highest next leading suit from current trick

                                    tally2v=tally2[next_ls]
                                    lis_t2=[]
                                    for a in tally2v:
                                        lis_t2.append(tally4[a])
                                    lis_t2=sorted(lis_t2)
                                    h_l2=max(lis_t2)
                                    list12=[]
                                    list13=[]
                                    for v in list11: #our sorted values of next_leading suit
                                        if v>h_l2:
                                            list12.append(v)
                                            for a,b in tally4.items():
                                                if b==list12[-1]:
                                                    l12=a
                                        else:         

                                            list13.append(v)
                                            for a,b in tally4.items():
                                                if b==list13[0]:
                                                    l13=a
                                    if list12!=[]: #if we have any value which is maximum of the next leading suit entry we will throw that else we throw minimum of that.
                                        return l12+next_ls
                                    else:
                                        return l13+next_ls

                                else:  
                                    tally_value=tally[deck_top[1]]
                                    list8=[]
                                    for b in tally_value:
                                        list8.append(tally4[b]) #list8 contains all elements of that trump suit
                                    
                                    m_tally=min(list8)
                                    #print(m_tally)
                                    for a,b in tally4.items():
                                        if b==m_tally:
                                            return a+deck_top[1]
                                
        
                                    
        else:
             
            if  curr_trick==() or curr_trick==[]:
                
                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0])) 
                
                list1=[]
                for a in sorted_list:
                    tally_value=tally4[a[0]]
                    list1.append((tally_value,a[-1]))
                list1=sorted(list1)
                
                
                for a,b in tally4.items():
                    if b==list1[-1][0]:
                        return a+list1[-1][1]
            elif player_no!=0:
                    next_ls=curr_trick[0][1]    #next leading suit of current tricks suit because we dont have that suit  
                    #print(next_ls)
                  #  print(curr_trick[0][1])
                    if next_ls==deck_top[1]:
                       # print("t")#we need to throw card of lowest suit.
                        if deck_top[1] in tally2.keys(): #if decks trump card matches with current trick




                            sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))#gets list sorted in ascending order
                            t2_v=(tally2.get(deck_top[1]))
                            t1_v=(tally.get(deck_top[1]) )
                            
                            if t2_v and t1_v:
                                l1=[]
                                l2=[]
                                for a in t2_v:
                                    l2.append(tally4[a])

                                l2_m=max(l2)
                                
                                for b in t1_v:
                                    l1.append(tally4[b])

                                l1_m=max(l1)
                                
                                if l1_m>l2_m:
                                    
                                    for a,b in tally4.items():
                                        if b==l1_m:
                                            return a+deck_top[1]
                                else:
                                    l1_v=l1[0]
                                    for a,b in tally4.items():
                                        if b==l1_v:
                                            return a+deck_top[1]
                            else:
                               
                                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                                list1=[]
                                for a in sorted_list:
                                    tally_value=tally4[a[0]]
                                    list1.append((tally_value,a[-1]))
                                list1=sorted(list1)
                                for a,b in tally4.items():
                                    if b==list1[0][0]:
                                        
                                        return a+list1[0][1]
                            
        
                    else: #if next leading suit is not same as decks trump card
                        #we need to throw card of next leading suit first than other. least 
                        #else throw ur max of next leading suit
                        list11=[]
                       # print("ri")
                        if  next_ls in tally.keys():
                            
                                
                            if next_ls in tally.keys():
                                tally_values=tally[next_ls]
                               # print(tally_values)
                                for a in tally_values:
                                    list11.append(tally4[a])
                                list11=sorted(list11)
                                for a,b in tally4.items():
                                    if b==list11[-1]:
                                        return a+next_ls
                            else:
                                tally_values=tally[deck_top[1]]
                                for a in tally_values:
                                    list11.append(tally4[a])
                                list11=sorted(list11)
                                
                                for a,b in tally4.items():
                                    if b==list11[-1]:
                                        return a+next_ls

                        else:#we have next leading suit but dont have trump card
                            list13=[]
                            for a in curr_trick:
                                list13.append(a[1])
                            #print(list13)
                            if deck_top[1] in list13:#if we have deck_top in current trick and we dont have that trump card we will throw smallest next_leading card else throw highest next leading card
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11)
                                    for a,b in tally4.items():
                                        if b==list11[0]:
                                            return a+next_ls
                                else:
                                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))
                                              
                                    list1=[]
                                    for a in sorted_list:
                                        tally_value=tally4[a[0]]
                                        list1.append((tally_value,a[-1]))
                                    list1=sorted(list1)
                                    for a,b in tally4.items():
                                        if b==list1[0][0]:
                                            return a+list1[0][1]
                            else:#dont have anhy trump card in current_trick . next_ls we need to throw and compared to current we need to throw






                                list11=[]
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11) #our values sortted of next_ls
                                    #we need highest next leading suit from current trick

                                    tally2v=tally2[next_ls]
                                    lis_t2=[]
                                    for a in tally2v:
                                        lis_t2.append(tally4[a])
                                    lis_t2=sorted(lis_t2)
                                    h_l2=max(lis_t2)
                                    list12=[]
                                    list13=[]
                                    for v in list11: #our sorted values of next_leading suit
                                        if v>h_l2:
                                            list12.append(v)
                                            for a,b in tally4.items():
                                                if b==list12[-1]:
                                                    l12=a
                                        else:         

                                            list13.append(v)
                                            for a,b in tally4.items():
                                                if b==list13[0]:
                                                    l13=a
                                    if list12!=[]: #if we have any value which is maximum of the next leading suit entry we will throw that else we throw minimum of that.
                                        return l12+next_ls
                                    else:
                                        return l13+next_ls
                                else:   
                                    
                                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                                    list1=[]
                                    for a in sorted_list:
                                        tally_value=tally4[a[0]]
                                        list1.append((tally_value,a[-1]))
                                    list1=sorted(list1)
                                    for a,b in tally4.items():
                                        if b==list1[0][0]:
                                            return a+list1[0][1]
        

                                    
            else: #if we are   at position 0 and we dont have any trump card. we will throw card of highest order.  #COMEBACK
                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))#gets list sorted in ascending order    
                
                #print(sorted_list)         
                list1=[]
                for a in sorted_list:
                    tally_value=tally4[a[0]]
                    list1.append((tally_value,a[-1]))
                list1=sorted(list1)
                for a,b in tally4.items():
                    if b==list1[0][0]:
                        return a+list1[-1][1]
            
                
    else:
     
        if  curr_trick==() or curr_trick==[]:
                
               
                
                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                list1=[]
                for a in sorted_list:
                    tally_value=tally4[a[0]]
                    list1.append((tally_value,a[-1]))
                list1=sorted(list1)
                for a,b in tally4.items():
                    if b==list1[0][0]:
                        return a+list1[0][1]
        
        
        elif player_no==0:
            
            sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
            list1=[]
            for a in sorted_list:
                tally_value=tally4[a[0]]
                list1.append((tally_value,a[-1]))
            list1=sorted(list1)
            for a,b in tally4.items():
                if b==list1[0][0]:
                    return a+list1[0][1]
        
        else:
           
           
            if player_no!=0:
                    next_ls=curr_trick[0][1]    #next leading suit of current tricks suit because we dont have that suit  
                   # print(next_ls)
                  #  print(curr_trick[0][1])
                    if next_ls==deck_top[1]:
                       # print("t")#we need to throw card of lowest suit.
                        if deck_top[1] in tally2.keys(): #if decks trump card matches with current trick


                            sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))#gets list sorted in ascending order
                            t2_v=(tally2.get(deck_top[1]))
                            t1_v=(tally.get(deck_top[1]) )
                            
                            if t2_v and t1_v:
                                l1=[]
                                l2=[]
                                for a in t2_v:
                                    l2.append(tally4[a])

                                l2_m=max(l2)
                                
                                for b in t1_v:
                                    l1.append(tally4[b])

                                l1_m=max(l1)
                                
                                if l1_m>l2_m:
                                    l1_v=l1[0]
                                    for a,b in tally4.items():
                                        if b==l1_v:
                                            return a+deck_top[1]
                                else:
                                    l1_v=l1[0]
                                    for a,b in tally4.items():
                                        if b==l1_v:
                                            return a+deck_top[1]
                            else:
                               
                                sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))           
                                list1=[]
                                for a in sorted_list:
                                    tally_value=tally4[a[0]]
                                    list1.append((tally_value,a[-1]))
                                list1=sorted(list1)
                                for a,b in tally4.items():
                                    if b==list1[-1][0]:
                                        return a+list1[-1][1]
                            
                                
                                    
                            
                            
                    else: #if next leading suit is not same as decks trump card
                        #we need to throw card of next leading suit first than other. least 
                        #else throw ur max of next leading suit
                        list11=[]
                        
                        if  next_ls in tally.keys():
                            
                                
                            if next_ls in tally.keys():
                                tally_values=tally[next_ls]
                               # print(tally_values)
                                for a in tally_values:
                                    list11.append(tally4[a])
                                list11=sorted(list11)
                                for a,b in tally4.items():
                                    if b==list11[-1]:
                                        return a+next_ls
                            else:
                                tally_values=tally[deck_top[1]]
                                for a in tally_values:
                                    list11.append(tally4[a])
                                list11=sorted(list11)
                                for a,b in tally4.items():
                                    if b==list11[-1]:
                                        return a+next_ls

                        else:#we have next leading suit but dont have trump card
                            
                            list13=[]
                            for a in curr_trick:
                                list13.append(a[1])

                            if deck_top[1] in list13:#if we have deck_top in current trick and we dont have that trump card we will throw smallest next_leading card else throw highest next leading card
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11)
                                    for a,b in tally4.items():
                                        if b==list11[0]:
                                            return a+next_ls
                                else:
                                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))
                                              
                                    list1=[]
                                    for a in sorted_list:
                                        tally_value=tally4[a[0]]
                                        list1.append((tally_value,a[-1]))
                                    list1=sorted(list1)
                                    for a,b in tally4.items():
                                        if b==list1[0][0]:
                                            return a+list1[0][1]
                            else:#dont have anhy trump card in current_trick . next_ls we need to throw and compared to current we need to throw





                                
                                list11=[]
                                if next_ls in tally.keys():
                                    tally_values=tally[next_ls]
                                    for a in tally_values:
                                        list11.append(tally4[a])
                                    list11=sorted(list11) #our values sortted of next_ls
                                    #we need highest next leading suit from current trick

                                    tally2v=tally2[next_ls]
                                    lis_t2=[]
                                    for a in tally2v:
                                        lis_t2.append(tally4[a])
                                    lis_t2=sorted(lis_t2)
                                    h_l2=max(lis_t2)
                                    list12=[]
                                    list13=[]
                                    for v in list11: #our sorted values of next_leading suit
                                        if v>h_l2:
                                            list12.append(v)
                                            for a,b in tally4.items():
                                                if b==list12[-1]:
                                                    l12=a
                                        else:         

                                            list13.append(v)
                                            for a,b in tally4.items():
                                                if b==list13[0]:
                                                    l13=a
                                    if list12!=[]: #if we have any value which is maximum of the next leading suit entry we will throw that else we throw minimum of that.
                                        return l12+next_ls
                                    else:
                                        return l13+next_ls
                                else:   
                                    sorted_list = sorted(hand, key=lambda tup: (tup[1], tup[0]))#gets list sorted in ascending order

                                            
                                    list1=[]
                                    for a in sorted_list:
                                        tally_value=tally4[a[0]]
                                        list1.append((tally_value,a[-1]))
                                    list1=sorted(list1)
                                    
                                    for a,b in tally4.items():
                                        
                                        if b==list1[-1][0]:
                                            return a+list1[-1][1]
















                            
                        
                            
                    
                    
                
                
            
            
            
            
        
        
   
        
    
    

    
        
    
    
    
    
    
    
    