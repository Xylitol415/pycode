'''
15-内置函数
1. cmp(item1, item2)
2.len()
3.max()
4.min()
5.del()
比较方式：
1. 引用地址的比较
   0x7fffffff => 引用地址  equals

2.具体数据的比较  ==
   18 == 19
3. === 绝对等于 引用地址、具体数值相同
'''

# 1.cmp 比较
name1 = "hello"
name2 = "world"
# cmp(name1, name2)
print("cmp:")

# 2.max()
ma = [18, 9, 7, 80]
print("最大数：", max(ma))

# 3.min()
ma = [18, 9, 7, 80]
print("最小数：", min(ma))

# 4.del
del ma[0]
print("删除后：", ma)
