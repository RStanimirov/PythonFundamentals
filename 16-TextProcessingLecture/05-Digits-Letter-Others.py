string_all_chars = input()

digits = []
letters = []
others = []

for x in string_all_chars:
    if x.isdigit():
        digits.append(x)
    elif x.isalpha():
        letters.append(x)
    else:
        others.append(x)

print(''.join(digits))
print(''.join(letters))
print(''.join(others))