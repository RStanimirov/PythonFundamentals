current_year = int(input())

while True:
    current_year += 1
    current_year_as_str = str(current_year)
    happy_year = True
    for i in range(len(current_year_as_str)):
        digit = current_year_as_str[i]
        for j in range(len(current_year_as_str)):
           if digit == current_year_as_str[j] and i != j:
               happy_year = False
               break
    if happy_year:
        print(current_year_as_str)
        break





