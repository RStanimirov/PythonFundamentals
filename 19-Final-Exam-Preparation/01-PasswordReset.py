raw_password = input()
command = input()
new_raw_password = ''

while command != "Done":
    data = command.split()
    action = data[0]

    if action == "TakeOdd":
        for i in range(len(raw_password)):
            if i % 2 != 0:
                new_raw_password += raw_password[i]
        print(new_raw_password)
        raw_password = new_raw_password

    elif action == "Cut":
        idx = int(data[1])
        length = int(data[2])
        first_part = raw_password[:idx]
        cut_part = raw_password[idx:idx + length]
        end_part = raw_password[idx + length::]
        raw_password = first_part + end_part
        print(raw_password)

    elif action == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {raw_password}")