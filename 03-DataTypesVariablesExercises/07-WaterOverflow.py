lines_n = int(input())
capacity = 255
next_liters = 0
filled_input = 0

for i in range(1, lines_n + 1):
    next_liters = int(input())

    if filled_input + next_liters > capacity:
        print('Insufficient capacity!')
    else:
        filled_input += next_liters

print(filled_input)