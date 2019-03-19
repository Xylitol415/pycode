x = "blue"
y = "green"
z = x
print(x,y,z) #print: blue green blue
z = y
print(x,y,z) #print: blue green green
x = z
print(x,y,z) #print: green green green

route = 866
print(route, type(route))
route = "North"
print(route, type(route))

phrase = "Wild Swans by Jung Chang"
print("J" in phrase)