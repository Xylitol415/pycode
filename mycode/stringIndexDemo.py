def extract_from_tag(tag,line):
	opener = "<" + tag + ">"
	closer = "</" + tag + ">"
	try:
		i = line.index(opener)
		start = i + len(opener)
		j = line.index(closer,start)
		return line[start:j]
	except ValueError:
		return None

def extract_from_tag1(tag,line):
	opener = "<" + tag + ">"
	closer = "</" + tag + ">"
	i = line.find(opener)
	if i != -1:
		start = i + len(opener)
		j = line.find(closer,start)
		if j != -1:
			return line[start:j]
	return None
s1 = extract_from_tag("red","what a <red>rose</red> this is")
s2 = extract_from_tag1("cute","what a <cute>dog</cute> this is")
print(s1)
print(s2)