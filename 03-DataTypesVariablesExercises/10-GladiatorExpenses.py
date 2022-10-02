lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

helmet_repair = 0
sword_repair = 0
shield_repair = 0
armour_repair = 0
total_repair = 0

helmet_count = 0
sword_count = 0
shield_count = 0
armour_count = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        helmet_count += 1
        helmet_repair = helmet_price * helmet_count
    if fight % 3 == 0:
        sword_count += 1
        sword_repair = sword_price * sword_count
    if fight % 2 == 0 and fight % 3 == 0:
        shield_count += 1
        shield_repair = shield_price * shield_count
        if shield_count % 2 == 0:
            armour_count += 1
            armour_repair = armour_price * armour_count

total_repair = helmet_repair + sword_repair + shield_repair + armour_repair

print(f"Gladiator expenses: {total_repair:.2f} aureus")

