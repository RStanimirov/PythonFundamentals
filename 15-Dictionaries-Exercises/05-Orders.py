command = input()

products_dict = {}

while command != "buy":
    data = command.split()
    product = data[0]
    price = float(data[1])
    qty = int(data[2])
    total_value = price * qty

    if product not in products_dict:
        products_dict[product] = []
    else:
        products_dict[product].append(price)
        products_dict[product].append(qty)



    command = input()

# for key, value in products_dict.items():
#     print(f"{key} -> {value:.2f}")

print(products_dict)