n = int(input())
available_cars = {}

for i in range(n):
    car_input = input().split("|")
    model = car_input[0]
    mileage = int(car_input[1])
    fuel = int(car_input[2])
    available_cars[model] = [mileage, fuel]

command = input()
while command != "Stop":
    data = command.split(" : ")
    action = data[0]
    if action == "Drive":
        model = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if available_cars[model][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            available_cars[model][0] += distance
            available_cars[model][1] -= fuel
            print(f"{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if available_cars[model][0] >= 100000:
                del available_cars[model]
                print(f"Time to sell the {model}!")

    elif action == "Refuel":
        model = data[1]
        fuel = int(data[2])

        if fuel > 75 - available_cars[model][1]:
            fuel = 75 - available_cars[model][1]

        available_cars[model][1] += fuel
        print(f"{model} refueled with {fuel} liters")

    elif action == "Revert":
        model = data[1]
        km = int(data[2])
        available_cars[model][0] -= km
        if available_cars[model][0] <= 10000:
            available_cars[model][0] = 10000
        else:
            print(f"{model} mileage decreased by {km} kilometers")

    command = input()

for key, value in sorted(available_cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")