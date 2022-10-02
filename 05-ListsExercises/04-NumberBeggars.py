coins_string = input()
beggars = int(input())

coins_list_as_str = coins_string.split(", ")
coins_list_as_int = list(map(int, coins_list_as_str))

beggars_list = [0] * beggars
counter = 0

for i in coins_list_as_int:
    beggars_list[counter] += i
    counter += 1
    if counter >= beggars:
        counter = 0

print(beggars_list)

# Below solution uses list comprehension for creating the list:
# coins_list = [int(num) for num in input().split(", ")]
# beggars = int(input())
# counter = 0
# beggars_list = [0] * beggars
#
# for i in coins_list:
#     beggars_list[counter] += i
#     counter += 1
#     if counter >= beggars:
#         counter = 0
#
# print(beggars_list)
