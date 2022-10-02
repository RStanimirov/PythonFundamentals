cards_list = input().split()
shuffle_times = int(input())

cards_list_length = len(cards_list)
cards_split = int(cards_list_length / 2)

for i in range(0, shuffle_times):
    shuffled_cards_list = []
    for j in range(0, cards_split):
        shuffled_cards_list.append(cards_list[j])
        shuffled_cards_list.append(cards_list[cards_split])
        cards_split += 1
    cards_list = shuffled_cards_list
    cards_split = int(cards_list_length / 2)

print(shuffled_cards_list)
