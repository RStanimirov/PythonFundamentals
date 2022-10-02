current_year = int(input())

while True:
    current_year += 1
    year_string = str(current_year)
    if len(year_string) == len(set(year_string)):
        print(current_year)
        break
