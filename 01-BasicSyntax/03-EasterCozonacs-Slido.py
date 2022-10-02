budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
price_for_one_cozonac = flour_price + eggs_price + milk_price

cozonacs = 0
colored_eggs = 0

while budget >= price_for_one_cozonac:
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= (cozonacs - 2)

    budget -= price_for_one_cozonac

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")