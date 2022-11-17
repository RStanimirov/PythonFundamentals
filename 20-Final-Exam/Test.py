# # Python3 code to demonstrate the
# # working of set() on list and tuple
#
# # initializing list
# lis1 = [3, 4, 1, 4, 5]
#
# # initializing tuple
# tup1 = (3, 4, 1, 4, 5)
#
# # Printing iterables before conversion
# print("The list before conversion is : " + str(lis1))
# print("The tuple before conversion is : " + str(tup1))
#
# # Iterables after conversion are
# # notice distinct and elements
# print("The list after conversion is : " + str(set(lis1)))
# print("The tuple after conversion is : " + str(set(tup1)))

command = input()
product_dict = {}

while command != "statistics":
    command_str = command.split(": ")
    product = command_str[0]
    quantity = command_str[1]

    if product not in product_dict.keys():
        product_dict[product] = int(quantity)
    else:
        product_dict[product] += int(quantity)
    command = input()

# print(product_dict)

print("Products in stock:")
for key, val in product_dict.items():
    print(f"- {key}: {val}")
print(f"Total products: {len(product_dict.keys())}")
print(f"Total quantity: {sum(product_dict.values())}")
