command = input()

notes_list = [0] * 11

while not command == 'End':
    note_splitted = command.split('-')
    note_priority = int(note_splitted[0])
    note_text = note_splitted[1]
    # notes_list.pop(note_priority)
    notes_list.insert(note_priority, note_text)
    command = input()

result = [x for x in notes_list if x != 0]
print(result)

# notes = [0] * 10
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split("-")
#     priority = int(tokens[0])
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# result = [x for x in notes if x != 0]
# print(result)
