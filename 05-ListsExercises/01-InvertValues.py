# string = input()
#
# numbers = string.split()
#
# numbers = [-int(x) for x in numbers]
#
# print(numbers)

numbers_str = input().split()
reversed_num_list = []

for num in numbers_str:
    reversed_num = int(num) * -1
    reversed_num_list.append(reversed_num)

print(reversed_num_list)
