"""
# while循环编写list值查找方法：
def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index



# for循环编写list值查找方法
def list_find(lst, target):
    for index, x in enumerate(lst):
        if x == target:
            break
    else:
        index = -1
    return index
"""
# 异常处理方法编写list查找


def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index


index = list_find(["1",2,"silly",-1,"M"], -1)
print(index)

