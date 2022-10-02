numbers_str = input().split()

numbers_list = []

for each_entry in numbers_str:
    numbers_list.append(int(each_entry))

removing_factor = int(input())

for i in range(removing_factor):
    numbers_list.remove(min(numbers_list))

print(', '.join(map(str, numbers_list)))

# numbers_str = input().split()
# remover = int(input())
# numbers_list = list(numbers_str)
# numbers_list_ints = list(map(int, numbers_list))
#
# for i in range(remover):
#     numbers_list_ints.remove(min(numbers_list_ints))
#
# print(", ".join(map(str, numbers_list_ints)))
