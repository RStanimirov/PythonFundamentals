email = input()
command = input()

while command != "Complete":
    data = command.split()
    action = data[0]

    if action == "Make":
        sub_action = data[1]
        if sub_action == "Upper":
            email = email.upper()
            print(email)
        elif sub_action == "Lower":
            email = email.lower()
            print(email)

    elif action == "GetDomain":
        count = int(data[1])
        # first_part = email[:len(email)-count]
        second_part = email[len(email)-count:]
        print(second_part)

    elif action == "GetUsername":
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            idx = email.find('@')
            first_part = email[:idx]
            print(first_part)

    elif action == "Replace":
        char = data[1]
        email = email.replace(char, '-')
        print(email)

    elif action == "Encrypt":
        for x in email:
            ord_value = ord(x)
            print(ord_value, end=' ')

    command = input()

