town_input = input()

city_population_gold_dict = {}
city = ''
population = 0
gold = 0

while town_input != "Sail":
    data = town_input.split('||')
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in city_population_gold_dict:
        city_population_gold_dict[city] = [population, gold]
    else:
        # city_population_gold_dict[city][0] += population
        city_population_gold_dict.get(city)[0] += population
        # city_population_gold_dict[city][1] += gold
        city_population_gold_dict.get(city)[1] += gold

    town_input = input()

# print(city_population_gold_dict)

command = input()

while command != "End":
    data = command.split("=>")
    action = data[0]
    if action == "Plunder":
        city = data[1]
        people_killed = int(data[2])
        stolen_gold = int(data[3])
        city_population_gold_dict[city][0] -= people_killed
        city_population_gold_dict[city][1] -= stolen_gold
        print(f"{city} plundered! {stolen_gold} gold stolen, {people_killed} citizens killed.")
        if city_population_gold_dict[city][0] <= 0 or city_population_gold_dict[city][1] <= 0:
            # del city_population_gold_dict[city]
            city_population_gold_dict.pop(city)
            print(f"{city} has been wiped off the map!")
    elif action == "Prosper":
        city = data[1]
        increased_gold = int(data[2])
        if increased_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_population_gold_dict[city][1] += increased_gold
            print(f"{increased_gold} gold added to the city treasury. {city} now has {city_population_gold_dict[city][1]} gold.")

    command = input()

if len(city_population_gold_dict) > 0:
    print(f"Ahoy, Captain! There are {len(city_population_gold_dict)} wealthy settlements to go to:")
    for key, value in sorted(city_population_gold_dict.items(), key=lambda x: (-x[1][1], x[0])):
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")