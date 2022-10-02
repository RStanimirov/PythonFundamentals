n = int(input())

plant_dict = {}

for i in range(n):
    plant_data = input().split('<->')
    plant_name = plant_data[0]
    rarity = int(plant_data[1])
    if plant_name not in plant_dict.keys():
        plant_dict[plant_name] = [rarity]
    else:
        plant_dict[plant_name][0] = rarity

# print(plant_dict)
command = input()

while command != "Exhibition":
    data = command.split()
    action = data[0]

    if action == "Rate:":
        plant_name = data[1]
        if plant_name not in plant_dict.keys():
            print("error")
        else:
            rating = int(data[3])
            plant_dict[plant_name].append(rating)

    elif action == "Update:":
        plant_name = data[1]
        if plant_name not in plant_dict.keys():
            print("error")
        else:
            new_rarity = int(data[3])
            plant_dict[plant_name][0] = new_rarity

    elif action == "Reset:":
        plant_name = data[1]
        if plant_name not in plant_dict.keys():
            print("error")
        else:
            plant_rarity = plant_dict[plant_name][0]
            plant_dict[plant_name].clear()
            plant_dict[plant_name].append(plant_rarity)

    command = input()

# print(plant_dict)

for key, value in plant_dict.items():
    if len(value) > 1:
        average = sum(value[1:]) / len(value[1:])
        # del plant_dict[key][1:]
        plant_dict[key] = [value[0]]
        plant_dict[key].append(average)
    else:
        plant_dict[key].append(0)

print("Plants for the exhibition:")
# print(plant_dict)
for key, value in sorted(plant_dict.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
