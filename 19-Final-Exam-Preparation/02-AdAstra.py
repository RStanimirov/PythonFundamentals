# # Below commented solution (RS) receives only 30 pts in Judge,
# # probably because keys are unique in dictionaries, and Judge expects
# # the food products to be printed on separate rows. If you have as input
# # three same products, let's say:
# # Bread#19/03/21#4000#|Invalid|03/03.20||Bread|19/03/21|4000||Bread|19/03/21|4000||Not right|6.8.20|5|
# # then what would happen ?
# import re
#
# text = input()
#
# pattern = r"(#|\|)([A-z][a-z]+|[A-z][a-z]+\s[A-z][a-z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
# matches = re.findall(pattern, text)
# food_dict = {}
# total_calories = 0
# # days_with_calories = 0
#
# for x in matches:
#     food_product = x[1]
#     expiry_date = x[2]
#     calories = int(x[3])
#
#     food_dict[food_product] = [expiry_date, calories]
#     total_calories += calories
#
# days_with_calories = total_calories // 2000
#
# print(f"You have food to last you for: {days_with_calories} days!")
# for key, value in food_dict.items():
#     print(f"Item: {key}, Best before: {value[0]}, Nutrition: {value[1]}")

import re

text = input()

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1"
matches = re.finditer(pattern, text)
food_list = []
total_calories = 0
days_with_calories = 0

for x in matches:
    food_product = x.group(2)
    best_before = x.group(3)
    calories = int(x.group(4))
    food_list.append([food_product, best_before, calories])
    total_calories += calories

days_with_calories = total_calories // 2000

print(f"You have food to last you for: {days_with_calories} days!")
for y in food_list:
    print(f"Item: {y[0]}, Best before: {y[1]}, Nutrition: {y[2]}")

