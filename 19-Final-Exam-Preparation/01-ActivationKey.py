activation_key = input()
command = input()

while command != "Generate":
    instruction_str = command.split('>>>')
    first_command = instruction_str[0]

    if first_command == "Contains":
        sub_string = instruction_str[1]
        if sub_string in activation_key:
            print(f"{activation_key} contains {sub_string}")
        else:
            print("Substring not found!")

    elif first_command == "Flip":
        upper_lower = instruction_str[1]
        start_idx = int(instruction_str[2])
        end_idx = int(instruction_str[3])
        sub_string = activation_key[start_idx:end_idx]
        first_part = activation_key[0:start_idx]
        last_part = activation_key[end_idx:]
        if upper_lower == "Upper":
            sub_string = sub_string.upper()
        else:
            sub_string = sub_string.lower()
        activation_key = first_part + sub_string + last_part
        print(activation_key)

    elif first_command == "Slice":
        start_idx = int(instruction_str[1])
        end_idx = int(instruction_str[2])
        first_part = activation_key[0:start_idx]
        last_part = activation_key[end_idx:]
        activation_key = first_part + last_part
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")