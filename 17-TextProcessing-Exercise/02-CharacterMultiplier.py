input_string = input().split()

str_1 = input_string[0]
str_2 = input_string[1]

min_length = min(len(str_1), len(str_2))
max_length = max(len(str_1), len(str_2))
current_sum = 0
total_sum = 0

for i in range(0, max_length):

    if i < len(str_1) and i < len(str_2):
        current_sum = ord(str_1[i]) * ord(str_2[i])
        total_sum += current_sum

    elif i < len(str_1) and i >= len(str_2):
        total_sum += ord(str_1[i])

    elif i >= len(str_1) and i < len(str_2):
        total_sum += ord(str_2[i])

print(total_sum)