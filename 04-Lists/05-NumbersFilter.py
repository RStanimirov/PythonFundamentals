n = int(input())
numbers_list = []
filtered_list = []

for i in range(n):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

if command == 'even':
    for number in numbers_list:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == 'odd':
    for number in numbers_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == 'negative':
    for number in numbers_list:
        if number < 0:
            filtered_list.append(number)
elif command == 'positive':
    for number in numbers_list:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)
