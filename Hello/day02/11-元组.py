'''
11-元组
元组 项目中固定值， 不容易修改的参数
不可修改元素
'''

student = (28, "张培培", 3.14)

# 修改  黄色背景代表语法错误，不可操作
# TypeError: 'tuple' object does not support item assignment
student[0] = 32
