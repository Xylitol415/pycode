'''
06-字符串常见操作
'''

name = '安庆市宜秀区大龙山镇集贤北路1318号'
names = '1318'
# 1.find() 查找下标  有--> 返回开始位置  没有-->-1
print(name.find(names))
# 2.index  查找下标 有--> 返回开始位置  没有-->异常
# print(name.index('520'))
# 3. count 统计次数
counts = "我爱我家，我是我家的人"
print('count:', counts.count("我"))
# print("count2: ", counts.count('我', start=5, end=10))
# 4.replace() 替换
# name 替换之后生成一个新的字符串
# 指向  字符串长度不可以 --> 方法区
# 内存区 引用地址
names4 = name.replace("大龙山", "二龙山")
print(names4)

# 5.split() 分隔符 得到list
na = name.split("大")
print("split分隔符：", na)

# url: http://www.baidu.com/request
url = "http://www.baidu.com/request"
urls = url.split("//")
print("url: ", urls)

# 6.startwith() 检查是否以obj开头
print(url.startswith("http://"))

# 7.小写
ns = "ABCDEF"
print("小写：", ns.lower())

# 8.大写
nss = "abcdef"
print("大写：", nss.upper())

# 9.lstrip() 删除左边空格
# 10.rstrip() 删除右边空格

# 11.join() 加入一个字符串
st = list("我是个")
ss = ""
st.append("帅哥")
sts = ss.join(st)
print(sts)

