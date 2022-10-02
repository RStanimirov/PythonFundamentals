import sys


def is_valid_index(collection: list, idx: int):
    if 0 <= idx < len(collection):
        return True
    return False


def exchange_list_at_index(collection: list, idx: int):
    exchanged_list = []
    if not is_valid_index(collection, idx):
        print("Invalid index")
        exchanged_list = collection
    else:
        left_sub_list = collection[:idx + 1]
        right_sub_list = collection[idx + 1:]

        for i in right_sub_list:
            exchanged_list.append(i)
        for i in left_sub_list:
            exchanged_list.append(i)

    return exchanged_list


def max_num(collection: list, custom_filter):
    # max_element = -sys.maxsize
    max_element = float('-inf')
    max_element_index = -1
    # Returns -1 if there is no match.
    # >= because the problem descriptions requires the "rightmost" element.
    for i in range(len(collection)):
        num = collection[i]
        if custom_filter(num) and num >= max_element:
            max_element = num
            max_element_index = i

    if max_element_index == -1:
        # No matches found.
        print("No matches")

    return max_element_index


def min_num(collection, custom_filter):
    min_element = sys.maxsize
    min_element_index = -1
    # Returns -1 if there is no match.
    # >= because the problem descriptions requires the "rightmost" element.
    for i in range(len(collection)):
        num = collection[i]
        if custom_filter(num) and num <= min_element:
            min_element = num
            min_element_index = i

    if min_element_index == -1:
        # No matches found.
        print("No matches")

    return min_element_index


def first_counted_elements(collection: list, cnt: int, custom_filter):
    if cnt > len(collection):
        print("Invalid count")
    else:
        matching_elements = []
        for num in collection:
            if custom_filter(num) and len(matching_elements) < cnt:
                matching_elements.append(num)

        print(matching_elements)


def last_counted_elements(collection: list, cnt: int, custom_filter):
    if cnt > len(collection):
        print("Invalid count")
    else:
        matching_elements = []
        for i in range(len(collection)-1, -1, -1):
            num = collection[i]
            if custom_filter(num) and len(matching_elements) < cnt:
                matching_elements.append(num)
        matching_elements = matching_elements[::-1]
        # We have to reverse back the list,because we had already reversed it above.
        print(matching_elements)


input_numbers = input().split()
numbers = [int(x) for x in input_numbers]

command = input()

while command != 'end':
    command_arguments = command.split()
    command_type = command_arguments[0]

    if command_type == 'exchange':
        index = int(command_arguments[1])
        numbers = exchange_list_at_index(numbers, index)

    elif command_type == 'max':
        command_filter = command_arguments[1]
        max_index = -1
        if command_filter == 'even':
            max_index = max_num(numbers, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            max_index = max_num(numbers, lambda n: n % 2 != 0)
        if max_index != -1:
            print(max_index)

    elif command_type == 'min':
        command_filter = command_arguments[1]
        min_index = -1
        if command_filter == 'even':
            min_index = min_num(numbers, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            min_index = min_num(numbers, lambda n: n % 2 != 0)
        if min_index != -1:
            print(min_index)

    elif command_type == 'first':
        count = int(command_arguments[1])
        command_filter = command_arguments[2]
        if command_filter == 'even':
            first_counted_elements(numbers, count, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            first_counted_elements(numbers, count, lambda n: n % 2 != 0)

    elif command_type == 'last':
        count = int(command_arguments[1])
        command_filter = command_arguments[2]
        if command_filter == 'even':
            last_counted_elements(numbers, count, lambda n: n % 2 == 0)
        elif command_filter == 'odd':
            last_counted_elements(numbers, count, lambda n: n % 2 != 0)

    command = input()

print(numbers)
