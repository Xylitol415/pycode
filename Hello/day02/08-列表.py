
'''
08-列表
1.添加元素
2.修改元素
3.查找元素
4.删除元素
'''
# 1.append 添加在元素最后面
# 2.extend

names = ["张半仙", "张安妮", "张艾嘉", "张宇"]
names.append("张三丰")
na = ["张无忌", "张惠妹"]
names.extend(na)
print(names)
# 3.insert
na.insert(0, "张培培")
print(na)

# 4.修改
names[0] = '张敏'
print(names)
#  5. in, not in
print("张敏" in names)
print("张家辉" not in names)

# 6.index 返回位置
print(names.index('张三丰'))

# 7.count 返回统计的数量
print(names.count('张敏'))

# 8.del 按下标删除
print("删除前：", names)
del names[0]
print("删除后：", names)

# 9.pop 删除最后一个元素
names.pop()
print("pop删除后：", names)

# 10. remove 根据元素删除
names.remove("张宇")
print("remove:", names)


