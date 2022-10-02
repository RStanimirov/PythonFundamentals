import re

command = input()
purchase_list = []
total_cost = 0

while command != "Purchase":
    purchase_list.append(command)
    command = input()

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(.\d+)?)!(?P<qty>\d+)"

print("Bought furniture:")

for x in purchase_list:
    match = re.finditer(pattern, x)
    for y in match:
        total_cost += float(y.group('price')) * int(y.group('qty'))
        print(y.group('furniture'))

print(f"Total money spend: {total_cost:.2f}")


