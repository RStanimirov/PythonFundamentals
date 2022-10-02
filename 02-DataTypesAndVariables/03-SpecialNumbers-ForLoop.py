my_number = int(input())
is_true = None
for i in range(1, my_number + 1):
    num_as_str = str(i)
    sum = 0
    for char in num_as_str:
        sum += int(char)
    if sum == 5 or sum == 7 or sum == 11:
        is_true = True
        print(f"{i} -> {is_true}")
    else:
        is_true = False
        print(f"{i} -> {is_true}")

