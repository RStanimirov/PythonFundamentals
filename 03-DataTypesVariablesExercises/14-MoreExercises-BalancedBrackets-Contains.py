number_of_lines = int(input())
opening_brackets_count = 0
closing_brackets_count = 0

for i in range(1, number_of_lines + 1):
    line = input()
    open_bracket= "("
    closing_bracket = ")"
    if line.__contains__(open_bracket):
        opening_brackets_count += 1
    if line.__contains__(closing_bracket):
        closing_brackets_count += 1
        if opening_brackets_count - closing_brackets_count != 0:
            break

if opening_brackets_count == closing_brackets_count:
    print("BALANCED")
else:
    print("UNBALANCED")
