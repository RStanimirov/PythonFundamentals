var_num = int(input())
is_special = None

for i in range(1, var_num + 1):
    sum_of_digits = 0
    number_sequence = i
    # To calculate the sum of digits, repeat the following: sum the last digit
    # (num % 10) and remove it (sum = sum / 10) until num reaches 0.

    while i > 0:
        sum_of_digits += i % 10
        i = int(i / 10)
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            is_special = True
        else:
            is_special = False

    print(f"{number_sequence} -> {is_special}")


