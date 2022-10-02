population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

if sum(population) < len(population) * minimum_wealth:
    print('No equal distribution possible')
    exit()
else:
    for country in population:
        if country < minimum_wealth:
            richest_country = max(population)
            needed_wealth = minimum_wealth - country
            index_of_richest_country = population.index(richest_country)
            index_of_country = population.index(country)
            population[index_of_richest_country] -= needed_wealth
            population[index_of_country] += needed_wealth

    print(population)
