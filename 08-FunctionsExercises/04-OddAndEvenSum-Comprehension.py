number_input = input()


def even_odd_func():
    even = [int(x) for x in number_input if int(x) % 2 == 0]
    odd = [int(x) for x in number_input if int(x) % 2 != 0]
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


print(even_odd_func())