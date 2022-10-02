product_and_price = input().split('|')
budget = int(input())
new_list = []
profit = 0
new_budget = 0

for product in product_and_price:
    token = product.split('->')
    item = token[0]
    price = float(token[1])
    if item == "Clothes" and price <= 50 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price
    elif item == "Shoes" and price <= 35 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price
    elif item == "Accessories" and price <= 20.50 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price

for i in new_list:
    print(f"{i:.2f}", end=" ")
print()

new_budget = sum(new_list) + budget
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
