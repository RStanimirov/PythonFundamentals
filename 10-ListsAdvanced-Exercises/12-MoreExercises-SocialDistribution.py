population = [int(x) for x in input().split(", ")]
wealth_min = int(input())

increase_counter = 0
reduced_wealth = 0

poor_country = []
average_country = []
advanced_country = []
donor_country = []

for country in population:
    if country < wealth_min:
        new_wealth = (wealth_min - country) + country
        increase_counter += (wealth_min - country)
        reduced_wealth = population[-1] - increase_counter
        if reduced_wealth < wealth_min * 2:
            reduced_wealth = population[-2] - increase_counter
        poor_country.append(new_wealth)

    if country == wealth_min:
        average_country.append(country)

    if country > wealth_min:
        if country != (reduced_wealth + increase_counter):
            advanced_country.append(country)
        else:
            donor_country.append(reduced_wealth)

print(poor_country + average_country + advanced_country + donor_country)
