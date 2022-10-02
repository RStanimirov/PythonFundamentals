import re

command = input()
text_line_list = []

# while True:
#     text_line = input()
#     text_line_list.append(text_line)
#     if not text_line:
#         break
while command:
    text_line_list.append(command)
    command = input()

text_as_string = ' '.join(text_line_list)

pattern = r"\d+"
valid_nums = re.findall(pattern, text_as_string)

print(*valid_nums)