import string


def letter_count(text, letters=string.ascii_letters):
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count

print(letter_count("Hello Python3.6"))
print(letter_count("Hello Python3.6", letters="aeiouAEIOU"))
