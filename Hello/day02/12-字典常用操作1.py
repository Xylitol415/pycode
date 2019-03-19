'''
12-字典常用操作
'''

student = {'name':'张三丰', 'age':18, 'sex':'男','number':'123'}

# 1. 修改元素
student['name'] = '张学友'
print(student)

# 2.添加元素
student.setdefault("id", '2733')
print(student)

# 3.删除元素 del(), clear()
del student['id']
print("del删除后：", student)

#清空整个字典
student.clear()
print("clear:", student)
