def price_func(product, qty):
    cost = 0
    if product == 'coffee':
        cost = 1.50 * qty
    elif product == 'water':
        cost = 1.00 * qty
    elif product == 'coke':
        cost = 1.40 * qty
    elif product == 'snacks':
        cost = 2.00 * qty
    return cost

my_product = input()
my_qty = int(input())

total_cost = price_func(my_product, my_qty)
print(f"{total_cost:.2f}")


