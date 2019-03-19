'''
02-函数
#无参函数


# 函数 println
def println():
    print("今天的天气好热啊！")

# 函数调用
println()
'''

# 求和
def sum(x, y):
    print("求和：", x + y)

sum(3, 12)

# 平均数
#  任何数除浮点数得浮点数
def avg(a, b, c):
    return (a+b+c)/3.0
num = avg(3,5,9)
print("avg = ", num)

# 信息
def info():
    return "张培培", 18

# 接收双返回值
name, age = info()
print("我的姓名是%s, 我的年龄是%d" % (name, age))
