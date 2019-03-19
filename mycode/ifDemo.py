lines = 10234
if lines<1000:
	print("small")
elif lines<10000:
	print("medium")
else:
	print("large")

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	if letter in "AEIOU":
		print(letter,"is a vowel")
	else:
		print(letter,"is a consonant")