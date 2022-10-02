import re

text = input()
matches_list = []
valid_matches = []
valid_output = []

pattern = r"(@|#)(?P<word>[A-Za-z]{3,})\1\1(?P<mirror>[A-Za-z]{3,})\1"
matches = re.finditer(pattern, text)

for x in matches:
    # print(x.group('word', 'mirror'))
    matches_list.append(x.group('word', 'mirror'))
    if x.group('word') == x.group('mirror')[::-1]:
        valid_matches.append(x.group('word', 'mirror'))

if len(matches_list) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches_list)} word pairs found!")

for y in valid_matches:
    valid_pair = y[0] + ' ' + '<=>' + ' ' + y[1]
    valid_output.append(valid_pair)

if len(valid_output) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(valid_output))