import math


def is_prime(x):
    s = math.sqrt(x)
    d = math.ceil(s)
    if s == d:
        d += 1
    for p in range(2, d):
        if x % p == 0:
            return False
    return True

prime = list()
composite = list()
for x in range(2,100):
    prime.append(x) if is_prime(x) == True else composite.append(x)
l = 0
print("prime number:")
while l < len(prime):
    print(prime[l], end=" ")
    l += 1
l = 0
print("\ncomposite number:")
while l < len(composite):
    if l!=0 and l%20 == 0:
        print("")
    print(composite[l], end=" ")
    l += 1
