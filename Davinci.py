
# coding: utf-8

# In[158]:

import random

# all deck list init
class Deck:
    deck = []
    def __init__(self):
        i = 0
        while i < 26:
            if(i == 24):
                self.deck.append([i,77,'검',0])
            elif(i == 25):
                self.deck.append([i,77,'흰',0])
            elif(i % 2 == 0):
                self.deck.append([i,int(i/2),'검',0]) 
            else:
                self.deck.append([i,int(i/2),'흰',0])
            i = i + 1


# player init
class player:
    nickname = "unknown",
    Hand = []
    Turn = 0
    Finded = 0
    Num_of_joker = 0 # 갖고있는 조커 카드수
    Last_card = []
    Get_pos = 0
    
 
# when a game is started, player 4_deck init
def Start(player1, deck):
        for i in range(4):
            j = random.randint(0,len(deck)-1)
            player1.Hand.append(deck[j])
            if deck[j][1] == 77:
                player1.Num_of_joker = player1.Num_of_joker + 1
            deck.remove(deck[j])
        player1.Hand.sort()
        player1.Last_card = player1.Hand[3]

def DetermineJoker(player1):
# 1. 조커를 새로운 카드로 받을 경우 - Lastcard에 deck[i][0] 저장
    if player1.Last_card[0] == 24 or player1.Last_card[0] == 25:
        return 1
    
# 2. 원래 있던 조커 순위 인덱스를 변경해야 할 경우 - 받을 수 있는 pos 2개로 한정
    elif player1.Num_of_joker != 0:
        Det = 0
        for i in range(len(player1.Hand)):
            if player1.Hand[i][0] == Last_card[0]:
                if i < len(player1.Hand) -1:
                    if player1.Hand[i+1][1] == 77:
                    
                if i > 0:    
                    if player1.Hand[i-1][1] == 77:    
                
        
        
        for i in range(len(player1.Hand)-3):
            if player1.Hand[i][1] == 77:
                if player1.Last_card[0] < player1.Hand[i][1] and player1.Hand[i+1][1] == 77:
                    player.Get_pos = i + 2
                    return 3
                    
        
        # 조커가 맨 앞에 있을 경우
        if player.Hand[0][1] == 77:
            if player.Hand[1][1] == 77:
                player1.Get_pos = 2
                return 
        # 조커가 맨 뒤에 있을 경우
        elif player1.Hand[len(player1.Hand)-1][1] == 77:
            if player1.Hand[len(player1.Hand)-2][1] == 77:
                player1.Get_pos = len(player1.Hand)+1
        else:
            for i in range(len(player1.Hand)-2):
                if player1.Hand[i][1] == 77:
                    if player1.Hand[i+1][1] == 77:
                        player1.Get_pos = i + 3
                        return 3
                    
                    player1.Get_pos = i + 1
                    break
        return 2
# 3. 그냥 넘어갈 경우
    else: 
        return 0
    
def CardPosition(player1, pos, Determined):
    if Determined == 1:
        if player1.Last_card[0] == 24:
            if pos == 1:
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[0][0] - 0.2
            elif pos == len(player1.Hand):
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[pos-2][0] + 0.2
            else:
                player1.Hand[len(player1.Hand)-1][0] = (player1.Hand[pos-2][0] + player1.Hand[pos-1][0]) / 2
        else:
            if pos == 1:
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[0][0] - 0.5
            elif pos == len(player1.Hand):
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[pos-2][0] + 0.5
            else:
                player1.Hand[len(player1.Hand)-1][0] = (player1.Hand[pos-2][0] + player1.Hand[pos-1][0]) / 2
        
    elif Determined == 2:
        if pos == player1.Get_pos:
            player1.Hand[player1.Get_pos-1][0] = player1.Hand[player1.Get_pos-1][0] + player1.Last_card[0] - player1.Hand[player1.Get_pos-2][0]
    
    player1.Hand.sort()
    print (player1.Hand)
    
    #elif Determined == 3:
        
    
def draw(player1, deck):
        j = random.randint(0,len(deck)-1)
        player1.Hand.append(deck[j])
        if deck[j][0] == 24 or deck[j][0] == 25:
            player1.Num_of_joker = player1.Num_of_joker + 1
        player1.Last_card = deck[j]
        deck.remove(deck[j])
        player1.Hand.sort()

def find(player1,pos,num):
        if player1.Hand[pos-1][3] == 1:
            print("이미 맞추셨습니다.")
            return
        flag = 0
        for i in range(len(player1.Hand)-1):
            if player1.Hand[i][1] == num and i == pos-1:
                flag = 1
                break
    
        if(flag == 0):
            player1.Turn = 0
            return 0
        else:
            player1.Turn = 1
            player1.Hand[i][3] = 1
            player1.Finded = player1.Finded + 1
            return 1

def hand_print(player1):
        prt = []
        for i in range(len(player1.Hand)):
            if player1.Hand[i][3] == 1:
                prt.append(player1.Hand[i][2]+str(player1.Hand[i][1]))
            else:
                prt.append(player1.Hand[i][2])
        print(prt)

def EndCheck(player1, player2):
        if player1.Finded == len(player1.Hand):
            print ("player2 Win")
            return 1
        elif player2.Finded == len(player2.Hand):
            print ("player1 Win")
            return 1
        else:
            return 0


# In[159]:

deck_cnt = 0
deck = Deck()
print(deck.deck)


# In[160]:

player1 = player()
Start(player1, deck.deck)

Determined = DetermineJoker(player1)

if player1.Num_of_joker == 2: # 첫번째 조커 위치
    while 1:
        pos = int(input('pos:'))
        if pos == 1 or pos == 2 or pos == 3:
            break
    CardPosition(player1, pos, Determined)
    player1.Last_card = player1.Hand[3]
        
print ('last:', player1.Last_card)
print ('joker:', player1.Num_of_joker)
print ('det:', Determined)
print ('player1:', player1.Hand)


# In[161]:

if Determined == 1:
    while 1:
        pos = int(input('pos:'))
        if 1 <= pos <= len(player1.Hand):
            if is_int(pos) == True:
                break
    CardPosition(player1, pos, Determined)
    
elif Determined == 2:
    while 1:
        pos = int(input('pos:'))
        if pos == player1.Get_pos - 1 or pos == player1.Get_pos:
            break
    CardPosition(player1, pos, Determined)

print ('last:', player1.Last_card)
print ('joker:', player1.Num_of_joker)
print ('det:', Determined)
print ('player1:', player1.Hand)


# In[162]:

draw(player1, deck.deck)
print ('p1:', player1.Hand)


# In[163]:

print (player1.Last_card)

