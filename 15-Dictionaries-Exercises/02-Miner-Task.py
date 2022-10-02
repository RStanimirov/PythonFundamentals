command = input()

resources_list = []
resources_dict = {}
key = ''
value = 0

while command != "stop":
    resources_list.append(command)

    command = input()

for i in range(0, len(resources_list), 2):
    key = resources_list[i]
    value = int(resources_list[i+1])

    if key not in resources_dict:
        resources_dict[key] = value
    else:
        resources_dict[key] += value

# print(resources_list)
# print(resources_dict)

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
