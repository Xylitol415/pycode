'''
04-输入函数
input()
'''
# 输入 input() 默认是str
name =  input("请输入您的姓名:")
QQ =  input("请输入您的QQ:")
phoneNum =  input("请输入您的手机号码:")
address =  input("请输入您的地址:")

# 类型转换 int --> str str --> int
# str() int()
QQ = int(QQ)
phoneNum = int(phoneNum)

# 输出
print("-"*50)
print("姓名：%s" % name)
print("qq:%d" % QQ)
print("手机号：%d" % phoneNum)
print("学校地址:%s" % address)
print("-"*50)
