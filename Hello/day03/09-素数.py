import math
def sushu():
    k = 1
    for m in range(100, 201):
        k = int(math.sqrt(m))
        for i in range(2, k) :
            if(m % i == 0):
                break
            else:
                print(m)
                break
            #flag = False
            #continue
    #if flag == True:
     #   print(m)
print(sushu())
