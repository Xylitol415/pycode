dictName = {}
Name = "hello world"
for n in Name:
    if n != " " and n not in dictName:
        dict.setdefault(n, Name.count(n))
    for key,value in dict.items():
        print("%s, %d"%(key, value), end=" ")

