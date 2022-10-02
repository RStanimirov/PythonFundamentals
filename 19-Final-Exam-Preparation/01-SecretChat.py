message = input()
command = input()

while command != "Reveal":
    data = command.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        idx = int(data[1])
        first_part = message[:idx]
        second_part = message[idx:]
        message = first_part + ' ' + second_part
        print(message)

    elif action == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            reverse_substring = substring[::-1]
            message = message + reverse_substring
            print(message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")


