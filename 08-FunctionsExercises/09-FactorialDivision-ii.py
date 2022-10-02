from math import factorial

number_1 = int(input())
number_2 = int(input())

factorial_num_1 = factorial(number_1)
factorial_num_2 = factorial(number_2)

result_division = factorial_num_1 / factorial_num_2

print(f"{result_division:.2f}")



