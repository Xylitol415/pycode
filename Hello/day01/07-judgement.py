
money = input("你有钱吗？")
house = input("你有房吗？")
save = input("你有存款吗？")
car = input("你有车吗？")
job = input("你有工作吗？")

money = int(money)
house = int(house)
save = int(save)
car = int(car)
job = int(job)

if money >= 100000:
    print("小伙子不错，考虑一下")
    if house >= 90:
        print("我是你女朋友了")
        if save >= 100000:
            print("我们去见爸妈吧")
            if car >= 100000:
                print("明天民政局见")
                if job >= 20000:
                    print("我们的孩子很漂亮")
                else:
                    print("我们性别不合适")
            else:
                print("我们衣服搭配不合适")
        else:
            print("我们星座不合适")
    else:
        print("我们性格不合适")
else:
    print("恩，你很优秀，我们不合适")


