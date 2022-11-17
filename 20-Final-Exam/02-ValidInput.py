n = int(input())

bosses_dict = {}

for i in range(n):
    input_str = input()
    data = input_str.split(':')
    raw_name = data[0]
    raw_profession = data[1]
    name = raw_name[1:-1]
    profession = raw_profession[1:-1]
    bosses_dict[name] = profession

for key, value in bosses_dict.items():
    split_value = value.split()
    if len(split_value) > 2:
        print("Access denied!")
    else:
        print(f"{key}, The {value}")
        print(f">> Strength: {len(key)}")
        print(f">> Armor: {len(value)}")
