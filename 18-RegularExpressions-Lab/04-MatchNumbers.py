import re

numbers_txt = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid_nums = re.finditer(pattern, numbers_txt)

for x in valid_nums:
    print(x.group(), end=' ')