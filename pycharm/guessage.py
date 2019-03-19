try:
    num = input("猜猜我的年龄：")
    age = int(num)
    while(age != 30):
        if(age > 30):
            print("大了")
        else:
            print("小了")
        num = input("继续:")
        age = int(num)
    print("正确")
except ValueError as err:
    print("请输入整数！")