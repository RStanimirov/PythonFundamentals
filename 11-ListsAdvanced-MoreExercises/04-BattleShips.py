rows_count = int(input())
destroyed_ships_count, ships = 0, []

for _ in range(rows_count):
    current_ships = [int(n) for n in input().split()]
    ships.append(current_ships)

command = input().split()

for i in range(len(command)):
    row = int(command[i][0])
    col = int(command[i][2])

    if ships[row][col] != 0:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            destroyed_ships_count += 1

print(destroyed_ships_count)