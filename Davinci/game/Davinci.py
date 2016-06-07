# coding: utf-8

# In[79]:

import random
 

# check int type
def is_int(x):
    if int(x) == x:
        return True
    else: 
        return False
 
 
# In[21]:
 
# all deck list init

# player init
class player:
    nickname = "unknown",
    Hand = []
    Turn = 0
    Finded = 0
    Num_of_joker = 0 # 갖고있는 조커 카드수
    Last_card = 0
    Get_pos = 0
    
 
# when a game is started, player 4deck init


def DetermineJoker(player1):
    Det = 0
    for i in range(len(player1.Hand)-1):
        if is_int(player1.Hand[i][0]) == False:
            if player1.Hand[i][0] < player1.Last_card < player1.Hand[i+1][0]:
                Det += 1
                break
            
# 1. 조커를 새로운 카드로 받을 경우 - Lastcard에 deck[i][0] 저장
    if player1.Last_card == 24 or player1.Last_card == 25:
        return 1
    
# 2. 원래 있던 조커 순위 인덱스를 변경해야 할 경우 - 받을 수 있는 pos 2개로 한정
    elif player1.Num_of_joker != 0 and Det != 0:
        # 조커가 맨 앞에 있을 경우
        if is_int(player.Hand[0][0]) == False:
            if is_int(player.Hand[1][0]) == True:
                player1.Get_pos = 2
        # 조커가 맨 뒤에 있을 경우
        elif is_int(player1.Hand[len(player1.Hand)-1][0]) == False:
            if is_int(player.Hand[len(player1.Hand)-1][0]) == True:
                player1.Get_pos = len(player1.Hand)+1
        else:
            for i in range(len(player1.Hand)-2):
                if is_int(player1.Hand[i]) == False:
                    if is_int(player1.Hand[i+1]) == False:
                        player1.Get_pos = i+3
                        return 3
                    
                    player1.Get_pos = i + 2
                    break
        return 2
# 3. 그냥 넘어갈 경우
    else: 
        return 0
    
def CardPosition(player1, pos, Determined):
    if Determined == 1:
        if player1.Last_card == 24:
            if pos == 1:
                player1.Hand[len(player1['Hand'])-1][0] = -1
            elif pos == len(player1.Hand):
                player1.Hand[pos-1][0] = player1.Hand[pos-2][0] + 0.2
            else:
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[pos-2][0] + 0.2
        else:
            if pos == 1:
                player1.Hand[len(player1.Hand)-1][0] = - 0.5
            elif pos == len(player1.Hand):
                player1.Hand[pos-1][0] = player1.Hand[pos-2][0] + 0.5
            else:
                player1.Hand[len(player1.Hand)-1][0] = player1.Hand[pos-2][0] + 0.5
        
    elif Determined == 2:
        if pos == player1.Get_pos:
            player1.Hand[player1.Get_pos-1][0] = player1.Hand[player1.Get_pos-1][0] + player1.Last_card - player1.Hand[player1.Get_pos-2][0]
    
    player1.Hand.sort()
    print (player1.Hand)
    
    #elif Determined == 3:
        
def Invert(a):
    if int(a) >= 10:
        a = a
    else:
        a = '0' + a
def draw(deck_cnt):
        j = random.randint(0,deck_cnt)

        return j
def SetTurn(player1, player2):
    if player1.Turn >= 1:
        player1.Turn = 0
        player2.Turn = 1
    else:
        player1.Turn = 1
        player2.Turn = 0
        
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
        if player1.Finded == player1.Hand_cnt:
            return 1
        elif player2.Finded == player2.Hand_cnt:
            print ("player1 Win")
            return 2
        else:
            return 0

