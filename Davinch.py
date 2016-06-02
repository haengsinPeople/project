
# coding: utf-8

# In[31]:

def Deck():
    i = 0
    deck = []
    while i<26:
        if(i == 24):
                deck.append([i,'joker','흑',0])
        elif(i == 25):
                deck.append([i,'joker','백',0])
        elif(i%2 == 0):
            
                deck.append([i,int(i/2),'흑',0]) 
        else:
                deck.append([i,int(i/2),'백',0])
        i = i +1
    return deck


# In[97]:

import random
def player1(mynum):
    player={'Playnum':mynum, 
          'PlayerName':"unknown", 
          'Hand':[],
          'Turn':0,
          'Hand_cnt':0,
          'Finded':0,
         }

    return player

def player2(mynum):
    player={'Playnum':mynum, 
          'PlayerName':"unknown", 
          'Hand':[],
          'Turn':0,
          'Hand_cnt':0,
          'Finded':0,
         }

    return player

def Start(player1, player2, deck):
        for i in range(0,4):
            j = random.randint(0,len(deck)-1)
            player1['Hand'].append(deck[j])
            deck.remove(deck[j])
            player1['Hand_cnt'] = player1['Hand_cnt'] + 1
        player1['Hand'].sort()
        
        for i in range(0,4):
            j = random.randint(0,len(deck)-1)
            player2['Hand'].append(deck[j])
            deck.remove(deck[j])
            player2['Hand_cnt'] = player2['Hand_cnt'] + 1
        player2['Hand'].sort()
        
        return deck_cnt
    
def draw(player1, deck):
        j = random.randint(0,len(deck)-1)
        player1['Hand'].append(deck[j])
        deck.remove(deck[j])
        player1['Hand_cnt'] = player1['Hand_cnt'] + 1
        
        player1['Hand'].sort()

def find(player1,pos,num):
        if player1['Hand'][pos-1][3] == 1:
            print("이미 맞추셨습니다.")
            return
        flag = 0
        for i in range(player1['Hand_cnt']):
            if player1['Hand'][i][1] == num and i == pos-1:
                flag = 1
                break
    
        if(flag == 0):
            player1['Turn'] = 0
            return 0
        else:
            player1['Turn'] = 1
            player1['Hand'][i][3] = 1
            player1['Finded'] = player1['Finded'] + 1
            return 1

def hand_print(player1):
        prt = []
        for i in range(player1['Hand_cnt']):
            if player1['Hand'][i][3] == 1:
                prt.append(player1['Hand'][i][2]+str(player1['Hand'][i][1]))
            else:
                prt.append(player1['Hand'][i][2])
        print(prt)

def EndCheck(player1, player2):
        if player1['Finded'] == player1['Hand_cnt']:
            print ("player2 Win")
            return 1
        elif player2['Finded'] == player2['Hand_cnt']:
            print ("player1 Win")
            return 1
        else:
            return 0


# In[98]:

deck_cnt = 0
deck = Deck()
print(deck)
player1 = player1(1)
player2 = player2(2)
Start(player1, player2, deck)
hand_print(player1)
hand_print(player2)
draw(player1, deck)
hand_print(player1)


# In[104]:

find(player1,5,11)
print(player1['Hand'])
hand_print(player1)
EndCheck(player1, player2)


# In[ ]:



