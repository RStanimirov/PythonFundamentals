command = input()

notes = [0] * 10

while not command == 'End':
    importance, text = command.split('-')
    current_index = int(importance) - 1
    notes[current_index] = text
    command = input()

print([x for x in notes if x != 0])
