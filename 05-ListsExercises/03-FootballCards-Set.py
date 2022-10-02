cards = set(input().split())

players_count_a = 11
players_count_b = 11
game_terminate = False

for i in cards:
    if 'A' in i:
        players_count_a -= 1

    elif 'B' in i:
        players_count_b -= 1

    if players_count_a < 7 or players_count_b < 7:
        game_terminate = True
        break

print(f"Team A - {players_count_a}; Team B - {players_count_b}")
if game_terminate:
    print('Game was terminated')