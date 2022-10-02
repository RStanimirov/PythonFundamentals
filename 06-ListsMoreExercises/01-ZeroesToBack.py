numbers_str = input().split(", ")

numbers_int = list(map(int, numbers_str))
filtered_list = []
zero_list = []
rearranged_list = []

for num in numbers_int:
    if num != 0:
        filtered_list.append(num)
    elif num == 0:
        zero_list.append(num)
    rearranged_list = filtered_list + zero_list

print(rearranged_list)

