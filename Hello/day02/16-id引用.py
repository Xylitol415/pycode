'''
16-id引用
'''
name1 = "Hello"
name2 = 'world'
print("name1:", id(name1))
print("name2:", id(name2))
print("比较：", name1 == name2)

name3 = "Hello"
name4 = 'Hello'
print("name3:", id(name3))
print("name4:", id(name4))
print("比较:", name3 == name4)


