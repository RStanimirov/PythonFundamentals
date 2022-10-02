def exchange_func(num_list, index_func):
    if (0 <= index_func) and index_func < len(num_list):
        first_part = num_list[index_func + 1:]
        second_part = num_list[:index_func + 1]
        exchanged_list = first_part + second_part
        return exchanged_list

    else:
        print("Invalid index")
        return num_list


def get_max_odd_index(num_list):
    num_list_odd = []
    for num in num_list:
        if num % 2 == 1:
            num_list_odd.append(num)
    for i in range(len(num_list) - 1, -1, -1):
        if len(num_list_odd) > 0:
            if num_list[i] == max(num_list_odd):
                print(i)
        else:
            print("No matches")
            break


def get_max_even_index(num_list):
    only_evens = []
    for el in num_list:
        if el % 2 == 0:
            only_evens.append(el)
    for i in range(len(num_list)):
        if len(only_evens) > 0:
            if num_list[i] == max(only_evens):
                print(i)
        else:
            print("No matches")
            break


def get_min_odd_index(num_list):
    num_list_odd = []
    for num in num_list:
        if num % 2 == 1:
            num_list_odd.append(num)
    for i in range(len(num_list) - 1, -1, -1):
        if len(num_list_odd) > 0:
            if num_list[i] == min(num_list_odd):
                print(i)
        else:
            print("No matches")
            break


def get_min_even_index(num_list):
    num_list_even = []
    for num in num_list:
        if num % 2 == 0:
            num_list_even.append(num)
    for i in range(len(num_list) - 1, -1, -1):
        if len(num_list_even) > 0:
            if num_list[i] == min(num_list_even):
                print(i)
        else:
            print("No matches")
            break


def get_first_even(num_list, count):
    while True:
        count_evens = []
        counter = 0
        if 0 > count or count > len(num_list):
            return "Invalid count"
        for i in num_list:
            if counter == count:
                break
            if i % 2 == 0:
                count_evens.append(i)
                counter += 1
        return count_evens


def get_first_odd(num_list, count):
    while True:
        count_odds = []
        counter = 0
        if 0 > count or count > len(num_list):
            return "Invalid count"
        for i in num_list:
            if counter == count:
                break
            if i % 2 == 1:
                count_odds.append(i)
                counter += 1
        return count_odds


def get_last_odd(num_list, count):
    while True:
        count_last_odds = []
        counter = 0
        if (0 > count) or (count > len(num_list)):
            return "Invalid count"
        for i in range(len(num_list) - 1, -1, -1):
            el = num_list[i]
            if counter == count:
                break
            if el % 2 == 1:
                count_last_odds.append(el)
                counter += 1
        return list(reversed(count_last_odds))


def get_last_even(num_list, count):
    while True:
        count_last_evens = []
        counter = 0
        if (0 > count) or (count > len(num_list)):
            return "Invalid count"
        for i in range(len(num_list) - 1, -1, -1):
            el = num_list[i]
            if counter == count:
                break
            if el % 2 == 0:
                count_last_evens.append(el)
                counter += 1
        return list(reversed(count_last_evens))


array_of_string = input().split()

numbers = list(map(int, array_of_string))

command = input()

while command != "end":
    token = command.split()
    command = token[0]
    if command == "exchange":
        index = int(token[1])
        numbers = exchange_func(numbers, index)
    elif command == "max":
        second_command = token[1]
        if second_command == "odd":
            (get_max_odd_index(numbers))
        elif second_command == "even":
            (get_max_even_index(numbers))
    elif command == "min":
        second_command = token[1]
        if second_command == "odd":
            (get_min_odd_index(numbers))
        elif second_command == "even":
            (get_min_even_index(numbers))
    elif command == "first":
        second_command = int(token[1])
        command_three = token[2]
        if command_three == "even":
            print(get_first_even(numbers, second_command))
        elif command_three == "odd":
            print(get_first_odd(numbers, second_command))
    elif command == "last":
        second_command = int(token[1])
        command_three = token[2]
        if command_three == "odd":
            print(get_last_odd(numbers, second_command))
        elif command_three == "even":
            print(get_last_even(numbers, second_command))
    command = input()

print(numbers)