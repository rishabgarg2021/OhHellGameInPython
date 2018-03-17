def score_phase(bids, tricks, deck_top, player_data=None, 
                suppress_player_data=True):
    from collections import defaultdict as dd
    # Implement this function.
    facecard=["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]
    tally1=dd(int)
    tally2={0: 0, 1: 0, 2: 0, 3: 0}
    j=2
    for i in facecard:  #makes dictionary with rank of facecards
        tally1[i]=j
        j+=1
    dd=dd(list)
    i=0
    order=[0, 1, 2, 3]
    list1=[]
    list2=[]
    tally={}
    for trick in tricks[:]:   
        #list1 is the list of all cards in phase with position
        for j in trick:
            list1.append((order[i], j))
            i=i+1
#makes dictionary tally which gives the bigram dictionary of each suit 
#with position and card with each player.
        for d in list1:
            if d[1][1] in tally:
                list2.append(d)
            
                tally[d[1][1]]+=list2
                list2 = []
            else:
                tally[d[1][1]]=[d]
        list4=[]
        #list4 is composed of all players position whos holding trump card
        for a, b in tally.items():
            #checks if it has that suit's deck card
            if a == deck_top[1]:
                list4.append(b)
        if list4!=[]:
            list5=[]
        #makes new list with position of player and that that decks 
        #matching card rank comparedd to tallly1.
            for y in list4:
                for z in y:
                    list5.append((tally1[z[1][0]], z[0]))
            list5=sorted(list5)
            pos_w=list5[-1][1] 
        #initialize every players point to zero and 1 if its winner
        #of that particular round.
            for i in range(4):
                pos_w=list5[-1][1]
                if i == pos_w:
                    tally2[pos_w]+=1 
            #position with score
            list1=[]
            list2=[]
            list4=[]
            list5=[]
            i=0
            if pos_w==1:
                order=[1, 2, 3, 0]
            elif pos_w==2:
                order=[2, 3, 0, 1]
            elif pos_w==3:
                order=[3, 0, 1, 2]
            else:
                order=[0, 1, 2, 3]
            tally={}
        else:
            # for loop determines the next leading suit of zeroth position
            new_suit=list1[0][1][1]
            list8=[]
        # gets cards with position of players which has that 
        #particular suit and  position.
            for a, b in tally.items():
                if a==new_suit:
                    list8.append(b)
            list9=[]
        #gets position of each player who has next leading suit 
        #and rank of theirr card
            for c in list8:
                for d, f in c:
                    list9.append((tally1[f[0]], d))
            list9=sorted(list9)
        #gets position of player who has next leading suit+ highest card of 
        #that particular suit
            pos_w=list9[-1][-1]
        #in same tally2 dictionary points are added of each player.
            for i in range(4):
                if i == pos_w:
                    tally2[pos_w]+=1 
            #position with score
            list1=[]
            list2=[]
            list4=[]
            list5=[]
            list8=[]
            list9=[]
            i=0
            tally={}
            if pos_w==1:
                order=[1, 2, 3, 0]
            elif pos_w==2:
                order=[2, 3, 0, 1]
            elif pos_w==3:
                order=[3, 0, 1, 2]
            else:
                order=[0, 1, 2, 3]
    tally2=tally2.items()
    list10=[]
    i=0
    for a, b in tally2:
        if bids[i]==b:
            b=b+10
        i+=1
        list10.append((b)) 
    return tuple(list10)
        
        
            
        
            
                
        
            
        
           
        
        
        
   
        
        
    
    
    
    
    
        
    
    
        
    
        
            
            
        
        
        