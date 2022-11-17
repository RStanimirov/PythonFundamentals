import re

n = int(input())

all_bosses_list = []
all_bosses_str = ''
valid_matches = {}
boss_name = ''

for i in range(n):
    boss_string = input()
    all_bosses_list.append(boss_string)
    for x in all_bosses_list:
        all_bosses_str = ', '.join(all_bosses_list)

# print(all_bosses_list)
# print(all_bosses_str)

pattern = r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#"
matches = re.finditer(pattern, all_bosses_str)

for x in matches:
    boss_name = x.group(1)
    boss_profession = x.group(2)
    valid_matches[boss_name] = boss_profession

for y in all_bosses_list:
    if boss_name in y:
        for key, value in valid_matches.items():
            print(f"{key}, The {value}")
            print(f">> Strength: {len(key)}")
            print(f">> Armor: {len(value)}")
    else:
        print("Access denied!")