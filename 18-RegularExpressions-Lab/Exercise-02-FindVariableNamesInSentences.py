import re

text = input()

pattern = r"(?<=\s)\_(?P<var_name>[a-zA-Z]+)\b"

# valid_variable = re.findall(pattern, text)
#
# list_valid_variables = []
#
# for x in valid_variable:
#     removed_underscore = x[1:]
#     list_valid_variables.append(removed_underscore)

valid_variable = re.finditer(pattern, text)
list_valid_variables = []

for x in valid_variable:
    list_valid_variables.append(x.group('var_name'))

print(','.join(list_valid_variables))