'''
08-匿名函数
'''
sum = lambda x, y : x + y
print (sum(3, 5))


def sum2(a, b, opt):
    print("a", a)
    print("b", b)
    print("opt", opt)
n = 7
s = 8
# 匿名引用地址  0x000000D3FB49CA60
# 十六进制引用地址值
sum2(3, 5, lambda n, s: n+s)


stus = [
    {"name":"zs", "age": "18"},
    {"name":"ls", "age": "19"},
    {"name":"ww", "age": "11"}
]

stus.sort(key = lambda x : x["age"])
print (stus)
