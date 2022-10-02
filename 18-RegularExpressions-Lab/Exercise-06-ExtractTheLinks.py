import re

text = input()
text_list = []

while text:
    text_list.append(text)
    text = input()

pattern = r"(www)\.([A-Za-z][A-Za-z0-9-]+)(\.[a-z]+)+"

for x in text_list:
    match = re.finditer(pattern, x)
    for y in match:
        print(y.group())


