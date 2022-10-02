input_string = input()

rearranged_string = ''
explosion_power = 0

for i in range(len(input_string)):
    if input_string[i] == '>':
        rearranged_string += '>'
        explosion_power += int(input_string[i+1])
    else:
        if explosion_power > 0:
            explosion_power -= 1
        else:
            rearranged_string += input_string[i]

print(rearranged_string)

