def sum(a,b,c):
    return a+b+c


def listsum(lst =None):
    lst = [] if lst is None else lst
    sum = 0
    for l in lst:
       sum += l
    return sum

l = [2,3,4,4,6,7,8]
print(listsum(l))
