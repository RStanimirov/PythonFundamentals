input_list = list(input().split())
nums_to_remove = int(input())

input_list_ints = list(map(int, input_list))

for i in range(nums_to_remove):
    min_num = min(input_list_ints)
    input_list_ints.remove(min_num)

print(', '.join(map(str, input_list_ints)))
