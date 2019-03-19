'''
14-字典的遍历
'''
student = {'name': '张三丰', 'age': 18, 'sex': '男', 'number': '123'}

# 1. 遍历key 获取所有的key
for key in student.keys():
    print(key, end=" ")
print()
# 2.遍历value 获取所有的value
for value in student.values():
    print(value, end=" ")
print()
# 3.遍历key，value 获取迭代所有的key value
for key,value in student.items():
    print(key, value, end=" ")
# 4. 遍历元素(key:value)
print()
for item in student.items():
    print(item, end=" ")
            