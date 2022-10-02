cities = {}

while True:
    data = input()
    if data == "Sail":
        break
    data = data.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city in cities:
        cities.get(city)[0] += population
        cities.get(city)[1] += gold
    else:
        cities[city] = [int(population), int(gold)]

# print(cities)
while True:
    line = input()
    if line == "End":
        break
    event = line.split("=>")
    action = event[0]
    if action == "Plunder":
        town = event[1]
        people = int(event[2])
        gold = int(event[3])
        cities.get(town)[0] -= people
        cities.get(town)[1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities.get(town)[0] <= 0 or cities.get(town)[1] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town = event[1]
        gold = int(event[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities.get(town)[1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities.get(town)[1]} gold.")
settlements = len(cities.keys())
cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
print(f"Ahoy, Captain! There are {settlements} wealthy settlements to go to:")
for k, v in cities.items():
    print(f"{k} -> Population: {cities.get(k)[0]} citizens, Gold: {cities.get(k)[1]} kg")