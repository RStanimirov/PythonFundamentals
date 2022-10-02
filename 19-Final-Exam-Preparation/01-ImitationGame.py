encrypted_message = input()
command = input()

while command != "Decode":
    data = command.split('|')
    action = data[0]

    if action == "Move":
        number_of_letters = int(data[1])
        part_to_move = encrypted_message[:number_of_letters]
        remaining_part = encrypted_message[number_of_letters:]
        encrypted_message = remaining_part + part_to_move
    elif action == "Insert":
        idx = int(data[1])
        value = data[2]
        first_part = encrypted_message[:idx]
        second_part = encrypted_message[idx:]
        encrypted_message = first_part + value + second_part
    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")