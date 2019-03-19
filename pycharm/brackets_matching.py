def is_balanced(text, brackets="()[]{}<>"):
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right
            if counts[left] == 0:
                return False
            counts[left] -= -1
    return not any(counts.values())

print(is_balanced("#include<stdio.h> void main(){printf('hello python'}"))
