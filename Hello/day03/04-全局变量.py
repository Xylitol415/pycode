'''
04-全局变量
作用范围 : .py文件
class 类范围中
'''
# 全局变量
name = "张培培"

def info():
    # 局部变量 --> 全局变量
    # 函数中对全局变量修改
    # 函数默认可以调用全局变量
    # 修改的话 global
    #global name = "张半仙"
    name = '张半仙'
    print("我的名字是：%s" % name)
def info2():
    print("帅哥的名字是：%s" % name)

info()
info2()
