initial_energy = 100
initial_coins = 100
events = input().split('|')
is_bankrupt = False

for event in events:
    event_info = event.split('-')
    event_type = event_info[0]
    event_value = int(event_info[1])

    if event_type == 'rest':
        energy_gained = event_value
        if initial_energy + event_value > 100:
            energy_gained = 100 - initial_energy

        initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == 'order':

        if initial_energy - 30 >= 0:
            initial_coins += event_value
            initial_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins - event_value > 0:
            initial_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            is_bankrupt = True
            break

if is_bankrupt == False:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
