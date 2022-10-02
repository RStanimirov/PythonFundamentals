year = float(input())

while True:
    year += 1
    year_to_str = str(year)
    if year_to_str[0] != year_to_str[1] and year_to_str[0] != year_to_str[2] and year_to_str[0] != year_to_str[3] and \
            year_to_str[1] != year_to_str[2] and year_to_str[1] != year_to_str[3] and year_to_str[2] != year_to_str[3]:
        break

print(f"{year:.0f}")