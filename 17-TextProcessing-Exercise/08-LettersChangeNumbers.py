#RS solution Letters Change Numbers, Text Processing Exercise, Jul 2021
input_list = input().split()

result = 0

for x in input_list:
    number = int(x[1:-1])
    if x[0].isupper():
        # If uppercase, divide the number by the letter's position.
        result += number / (ord(x[0])-64)
    elif x[0].islower():
        # If lowercase, multiply the number with the letter's position.
        result += number * (ord(x[0]) - 96)

    if x[-1].isupper():
        # If uppercase, subtract its position from the resulted number.
        result -= (ord(x[-1]) - 64)
    elif x[-1].islower():
        # If lowercase, add its position to the resulted number.
        result += (ord(x[-1]) - 96)

print(f"{result:.2f}")

