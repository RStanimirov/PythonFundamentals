coins_list = [int(x) for x in input().split(", ")]
number_of_beggars = int(input())
# Create beggars list with as many zeroes as the number of beggars,
# so that afterwards during the loop teh zeroes can be filled with values,
# depending on the beggars' turn:
beggars_list = [0] * number_of_beggars
# the first loop iterates over each beggar, current beggar = i
# the second loop iterates over the coins list which will be distributed to the beggars
# depending on their turn.
# If current coin is divisible by the current beggar without remainder, that means it's
# the current beggar's turn; the "if beggars_list[i] == 0" checks if there are coins left;
# the next beggars will receive zero coins if no coins are left.
# This loop "if beggars_list[i] == 0" is used to check if
# the beggars (turns) are more than the coins sequence.

for i in range(len(beggars_list)):
    current_beggar = i
    for j in range(len(coins_list)):
        current_coin = j % number_of_beggars
        if current_coin == current_beggar:
            if beggars_list[i] == 0:
                if coins_list[j] == 0:
                    beggars_list[current_coin] = 0
                    break
                beggars_list[current_coin] = coins_list[j]
            else:
                beggars_list[current_coin] += coins_list[j]

print(beggars_list)
