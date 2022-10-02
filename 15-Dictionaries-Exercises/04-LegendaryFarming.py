materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}

is_obtained = False

while True:
    list_of_materials = input().lower().split()

    for i in range(0, len(list_of_materials), 2):
        qty = int(list_of_materials[i])
        material = list_of_materials[i+1]

        if material == "shards":
            materials_dict[material] += qty
            if materials_dict[material] >= 250:
                materials_dict[material] -= 250
                print("Shadowmourne obtained!")
                is_obtained = True
                break

        elif material == "fragments":
            materials_dict[material] += qty
            if materials_dict[material] >= 250:
                materials_dict[material] -= 250
                print("Valanyr obtained!")
                is_obtained = True
                break

        elif material == "motes":
            materials_dict[material] += qty
            if materials_dict[material] >= 250:
                materials_dict[material] -= 250
                print("Dragonwrath obtained!")
                is_obtained = True
                break

        else:
            if material not in junk_dict:
                junk_dict[material] = 0
            junk_dict[material] += qty

    if is_obtained:
        break

sorted_key_materials = dict(sorted(materials_dict.items(), key=lambda x: (-x[1], x[0])))
for key, value in sorted_key_materials.items():
    print(f"{key}: {value}")

sorted_junk_materials = dict(sorted(junk_dict.items(), key=lambda x: x[0]))
for key, value in sorted_junk_materials.items():
    print(f"{key}: {value}")
