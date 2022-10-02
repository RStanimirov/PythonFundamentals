input_sequence = input().split()
bakery_dict = {}

for i in range(0, len(input_sequence), 2):
    key = input_sequence[i]
    value = input_sequence[i + 1]
    bakery_dict[key] = int(value)

print(bakery_dict)
