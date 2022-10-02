number_of_lines = int(input())
opening_brackets_count = 0
closing_brackets_count = 0
is_balanced = True

for i in range(1, number_of_lines + 1):
    line_string = input()
    if line_string == "(":
        opening_brackets_count += 1
    elif line_string == ")":
        closing_brackets_count += 1
    if closing_brackets_count > opening_brackets_count:
        is_balanced = False
        break
    elif opening_brackets_count - 1 > closing_brackets_count:
        is_balanced = False
        break

if opening_brackets_count == closing_brackets_count:
    is_balanced = True
else:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")