cards_input = input().split()
shuffle_times = int(input())
# Use // instead of / because in Python / receives a floating point value !
half_size = len(cards_input) // 2

for i in range(shuffle_times):
    left_part = cards_input[0:half_size]
    right_part = cards_input[half_size:len(cards_input)]
    shuffled_cards = []

    for j in range(len(left_part)):
        shuffled_cards.append(left_part[j])
        shuffled_cards.append(right_part[j])
    # Below line is necessary so that the cards one shuffled once, can be
    # shuffled a second time, third time and so on as per the shuffle_times value.
    cards_input = shuffled_cards

    print(cards_input)
