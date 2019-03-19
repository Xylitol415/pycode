def f(x, l = None):
    l = l if l is not None else[]
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3)
f(3,[3,2,1])
f(4)