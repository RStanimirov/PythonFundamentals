max_energy = 100
energy = 100
coins = 100
events_str = input().split('|')

for event in events_str:
    type_of_event, value = event.split('-')
    value = int(value)
    if type_of_event == 'rest':
        gained = min(value, max_energy - energy)
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')

    elif type_of_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        coins -= value
        if coins > 0:
            print(f'You bought {type_of_event}.')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            break

if coins > 0:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')