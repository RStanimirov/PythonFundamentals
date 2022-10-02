budget = float(input())
flour_price_one_kg = float(input())

eggs_price_one_pack = flour_price_one_kg * 75 / 100
milk_price_one_l = flour_price_one_kg + (25 * flour_price_one_kg / 100)

kozonac_one_pc = eggs_price_one_pack + flour_price_one_kg + (milk_price_one_l / 4)

kozonacs_counter = 0
coloured_eggs = 0

while budget - kozonac_one_pc > 0:
    kozonacs_counter += 1
    budget -= kozonac_one_pc
    coloured_eggs += 3
    if kozonacs_counter % 3 == 0:
        coloured_eggs -= kozonacs_counter - 2

print(f"You made {kozonacs_counter} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")


