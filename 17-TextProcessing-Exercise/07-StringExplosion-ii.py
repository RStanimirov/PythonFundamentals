string_input = input()

rearranged_str = ''
explosion = 0

for i in range(len(string_input)):
    if string_input[i] != '>':
        if explosion == 0:
            rearranged_str += string_input[i]
        else:
            explosion -= 1

    elif string_input[i] == '>':
        explosion += int(string_input[i + 1])
        rearranged_str += '>'

print(rearranged_str)
