# RS solution Rage Quit, Text processing exercise, Jul 2021
import re

input_string = input().upper()

splitted_input = re.split(r"(\d+)", input_string)
# print(splitted_input)
result_list = []

for i in range(0, len(splitted_input)-1, 2):
    string_to_repeat = splitted_input[i]
    repeat_times = int(splitted_input[i+1])
    result_list.append(string_to_repeat * repeat_times)

result_to_print = ''.join(result_list)
unique_characters = len(set(result_to_print))

print(f"Unique symbols used: {unique_characters}")
print(result_to_print)
