"""
   Craps赌博游戏
   我们设定玩家开始游戏时有1000元的赌注
   游戏结束的条件是玩家输光所有的赌注
   
   Version: 0.1
   Author: 骆昊
"""

from random import randint

money = 1000
while money > 0:
    print("你的总资产为: %d元" % money)
    needs_go_on = False
    while True:
        debt = int(input("请下注: "))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print("玩家摇出了%d点" % first)
    if first == 7 or first == 11:
        print("玩家胜!")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜!")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print("玩家摇出了%d点" % current)
        if current == 7:
            print("庄家胜!")
            money -= debt
            needs_go_on = False
        elif current == first:
            print("玩家��!")
            money += debt
            needs_go_on = False
        else:
            needs_go_on = True

print('你破产了, 游戏结束!')
        