# NOTE: below solution works only 80/100 in Judge.
card_string = input()
card_list = list(card_string.split())

team_a = 11
team_b = 11
is_terminated = False
for i in card_list:
    if 'A' in i:
        team_a -= 1
        if team_a < 7:
            is_terminated = True
            break
    elif 'B' in i:
        team_b -= 1
        if team_b < 7:
            is_terminated = True
            break

print(f"Team A - {team_a}; Team B - {team_b}")
if is_terminated:
    print("Game was terminated")
