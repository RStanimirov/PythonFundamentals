import re

text = input()
valid_destinations_list = []
travel_points = 0

pattern = r"(=|\/)(?P<location>[A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, text)

for x in matches:
    valid_destinations_list.append(x[1])
    travel_points += len(x[1])

print(f"Destinations: {', '.join(valid_destinations_list)}")
print(f"Travel Points: {travel_points}")
