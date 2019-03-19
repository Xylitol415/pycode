'''
不定长参数
*args  传入未命名的参数
**kwargs  传入已经命名的参数
'''
def fun(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("*args:", args)
    print("**kwargs:", kwargs)
fun(3, 5, 7, 8, 9, n = 12, p = 15, q = 25)