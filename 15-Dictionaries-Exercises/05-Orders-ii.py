command = input()

price_and_product = {}
qty_and_product = {}

while command != "buy":
    data = command.split()
    product = data[0]
    price = float(data[1])
    qty = int(data[2])

    if product not in qty_and_product:
        qty_and_product[product] = 0
    qty_and_product[product] += qty

    if product not in price_and_product:
        price_and_product[product] = 0
    price_and_product[product] = price

    command = input()

# print(price_and_product)
# print(qty_and_product)
#
# for x in qty_and_product:
#     print(f"{x} -> {(qty_and_product[x] * price_and_product[x]):.2f}")
for key, value in qty_and_product.items():
    product = key
    qty = value
    price = price_and_product[product]
    total_value = price * qty
    print(f"{product} -> {total_value:.2f}")
