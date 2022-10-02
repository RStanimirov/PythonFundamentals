stock_items = input().split()
warehouse = {}

for i in range(0, len(stock_items), 2):
    key = stock_items[i]
    value = stock_items[i+1]
    warehouse[key] = int(value)

searched_products = input().split()

for x in searched_products:
    if x in warehouse:
        print(f"We have {warehouse[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")

