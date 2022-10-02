gifts = input()
command = input()
gifts_list = gifts.split()
gifts_filtered_list = []
while command != "No Money":
    command_list = command.split()
    if command_list[0] == "OutOfStock":
        for gift in gifts_list:
            if gift == command_list[1]:
                index = gifts_list.index(gift)
                gifts_list[index] = "None"

    elif command_list[0] == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_list[1]

    elif command_list[0] == "JustInCase":
        index = len(gifts_list) - 1
        gifts_list[index] = command_list[1]

    command = input()

for elements in gifts_list:
    if elements != "None":
        gifts_filtered_list.append(elements)

print(" ".join(gifts_filtered_list))
