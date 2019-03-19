'''
九九乘法表
'''

j = 1
while j <= 9:
    i = 1
    while i <= 9:
        if i < j:
            print(i, "*", j, "=", i * j, end="  ")
        if i == j:
            print(i, "*", j, "=", i * j)
        i += 1
    j += 1

