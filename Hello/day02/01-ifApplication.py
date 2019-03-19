'''
练习：猜数字游戏
'''


import random
num = random.randint(0, 100)
while True:
    userNum = int(input("请输入您要猜的数字："))
    if userNum > num:
        print("您猜大了！")
    elif userNum < num:
        print("您猜小了！")
    elif userNum == num:
        print("您猜对了！")
        break
    else:
        print("输入格式错误！")
