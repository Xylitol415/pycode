def sum(a, b):
    a += b
a = 3
b = 5
sum(a, b)
print("a b:%d %s" % (a, b))


lt = [3, 5]
def sum2(lt):
    lt[0] = 300
lt = [3, 5]
sum2(lt)
print("可变类型：", lt)
