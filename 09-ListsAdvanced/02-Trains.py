number_wagons = int(input())
train_list = [0] * number_wagons

command = input()

while command != 'End':
    data = command.split()
    if data[0] == 'add':
        n_people = int(data[1])
        train_list[-1] += n_people
    elif data[0] == 'insert':
        n_people = int(data[2])
        wagon_index = int(data[1])
        train_list[wagon_index] += n_people
    elif data[0] == "leave":
        n_people = int(data[2])
        wagon_index = int(data[1])
        train_list[wagon_index] -= n_people

    command = input()

print(train_list)
