all_materials = input().split()

key_materials = {'motes': 0, 'shards': 0, 'fragments': 0}
junk_materials = {}

is_obtained = False

while not is_obtained:
    for i in range(0, len(all_materials), 2):
        qty = int(all_materials[i])
        item = all_materials[i+1].lower()

        if item in key_materials:
            key_materials[item] += qty

            if item == "motes":
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Dragonwrath obtained!')
                    is_obtained = True
                    break

            elif item == "fragments":
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Valanyr obtained!')
                    is_obtained = True
                    break

            elif item == "shards":
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Shadowmourne obtained!')
                    is_obtained = True
                    break

        else:
            if item in junk_materials:
                junk_materials[item] += qty
            else:
                junk_materials[item] = qty

    if is_obtained:
        break

    all_materials = input().split()


key_materials_sorted = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
junk_materials_sorted = sorted(junk_materials.items(), key=lambda x: x[0])

for material, quantity in key_materials_sorted:
    print(f"{material}: {quantity}")
for material, quantity in junk_materials_sorted:
    print(f"{material}: {quantity}")

