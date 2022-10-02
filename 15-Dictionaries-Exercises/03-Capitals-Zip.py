countries_list = input().split(", ")
capitals_list = input().split(", ")

zipped_dict = dict(zip(countries_list, capitals_list))

for x, y in zipped_dict.items():
    print(f"{x} -> {y}")

