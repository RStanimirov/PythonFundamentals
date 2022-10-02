string_input = input().split()
initial_sequence = list(map(int, string_input))
step_turn = int(input())

chosen_list = []
counted = 0

index = 0
while len(initial_sequence) > 0:
    counted += 1
    if counted % step_turn == 0:
        chosen_list.append(initial_sequence.pop(index))
    else:
        index += 1

    if index >= len(initial_sequence):
        index = 0

print(str(chosen_list).replace(' ', ''))
