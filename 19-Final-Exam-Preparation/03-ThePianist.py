number_of_pieces = int(input())

pieces_dict = {}

for i in range(number_of_pieces):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    piece_key = data[2]
    pieces_dict[piece] = [composer, piece_key]

command = input()

while command != "Stop":
    command_data = command.split('|')
    action = command_data[0]

    if action == "Add":
        piece = command_data[1]
        composer = command_data[2]
        key = command_data[3]
        if piece not in pieces_dict:
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        piece = command_data[1]
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        piece = command_data[1]
        new_key = command_data[2]
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

pieces_dict = sorted(pieces_dict.items(), key=lambda x: (x[0], x[1][0]))
for key, value in pieces_dict:
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
