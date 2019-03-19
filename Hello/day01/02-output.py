'''
02-输出
print()
'''
age = 18
print("我的年龄是", age)
#格式化输出1
print("我的年龄是%d岁" % age)
#格式化输出2  %f
name = "方鑫"
print("我的姓名是%s,今年是%d岁" % (name, age))
#\n 换行输出
print("亚洲四大邪术\n我一个都不会。")


#03-输出练习
name = "方鑫"
QQ = 1173950721
phoneNum = 18325604325
address = "安徽省安庆市宜秀区大龙山镇"

print("-"*50)
print("姓名：%s" %name)
print("qq:%d" %QQ)
print("手机号：%d" %phoneNum)
print("学校地址:%s" %address)
print("-"*50)