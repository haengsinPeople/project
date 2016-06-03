
# coding: utf-8

# In[ ]:



import random


# In[ ]:

# check int type
def is_int(x):
    if int(x) == x:
        return True
    else: 
        return False


# In[ ]:




# In[ ]:

# all deck list init
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

# player init
def player1(mynum):
    player={'Playnum':mynum, 
          'PlayerName':"unknown", 
          'Hand':[],
          'Turn':0,
          'Hand_cnt':0,
          'Finded':0,
          'Num_of_joker':0, # 갖고있는 조커 카드수
          'Last_card':0,
          'Get_pos':NULL,
         }

    return player

def player2(mynum):
    player={'Playnum':mynum, 
          'PlayerName':"unknown", 
          'Hand':[],
          'Turn':0,
          'Hand_cnt':0,
          'Finded':0,
          'Num_of_joker':0,
          'Last_card':0,
          'Get_pos':NULL,
         }

    return player

# when a game is started, player 4deck init
def Start(player1, deck):
        for i in range(0,4):
            j = random.randint(0,len(deck)-1)
            player1['Hand'].append(deck[j])
            if player1['Hand'][0] == 24 or player1['Hand'][0] == 25:
                player1['Num_of_joker'] = player1['Num_of_joker'] + 1
            deck.remove(deck[j])
            player1['Hand_cnt'] = player1['Hand_cnt'] + 1
        player1['Hand'].sort()
        
        return deck_cnt

def DetermineJoker(player1):
    Det = 0
    for i in range(len(player1['Hand'])-1):
        if is_int(player1['Hand'][0][i]) == False:
            if player1['Hand'][0][i] < player1['Last_card'] < player1['Hand'][0][i+1]:
                Det += 1
                break
            
# 1. 조커를 새로운 카드로 받을 경우 - Lastcard에 deck[0] 저장
    if player1['Last_card'] == 24 or 25:
        return 1
    
# 2. 원래 있던 조커 순위 인덱스를 변경해야 할 경우 - 받을 수 있는 pos 2개로 한정
    elif player1['Num_of_joker'] != 0 and Det != 0:
        # 조커가 맨 앞에 있을 경우
        if is_int(player['Hand'][0][0]) == False:
            player1['Get_pos'] = 2
        # 조커가 맨 뒤에 있을 경우
        elif is_int(player1['Hand'][0][len(player1['Hand'])-1]) == False:
            player1['Get_pos'] = len(player1['Hand'])-1
        else:
            for i in range(len(player1['Hand'])-1):
                if is_int(player1['Hand'][i]) == False:
                    player1['Get_pos'] = i + 1
                    break
        return 2
# 3. 그냥 넘어갈 경우
    else: 
        return 0
    
def CardPosition(player1, pos, Determined):
    if Determined == 1:
        if player1['Last_card'] == 24:
            if pos == 1:
                player1['Hand'][len(player1['Hand'])-1][0] = -1
            elif pos == len(player1['Hand']-1):
                player1['Hand'][pos][0] == player1['Hand'][pos-1][0] + 0.2
            else:
                player1['Hand'][len(player1['Hand'])-1][0] = player1['Hand'][pos-1][0] + 0.2
        else:
            if pos == 1:
                player1['Hand'][i][0] = - 0.5
            elif pos == len(player1['Hand']-1):
                player1['Hand'][pos][0] == player1['Hand'][pos-1][0] + 0.5
            else:
                player1['Hand'][len(player1['Hand'])-1][0] = player1['Hand'][pos-1][0] + 0.5
        
    elif Determined == 2:
        if pos == player1['Get_pos']:
            player1['Hand'][player1['Get_pos']-1][0] = player1['Hand'][player1['Get_pos']-1][0] + player1['Last_card'] - player1['Hand'][player1['Get_pos']-2][0]
    player1['Hand'].sort()
    
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


# In[ ]:

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


# In[ ]:

find(player1,5,11)
print(player1['Hand'])
hand_print(player1)
EndCheck(player1, player2)

