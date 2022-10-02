word = list(input())

numbers = []
take_list = []
skip_list = []
non_numbers = []
skip_index = 0
result = ''

for i in range(len(word)):
    if word[i].isdigit():
        numbers.append(word[i])
    else:
        non_numbers.append(word[i])

for i in range(len(numbers)):
    if i % 2 == 0:
        take_list.append(numbers[i])
    else:
        skip_list.append(numbers[i])

for i in range(len(take_list)):
    take = int(take_list[i])
    skip = int(skip_list[i])

    if skip_index + take > len(non_numbers):
        take = len(non_numbers) - skip_index

    for i in range(take):
        result += non_numbers[skip_index + i]

    skip_index += int(take) + skip

print(result)