# Car Race (Lists, More Exercises), RS Jun 2021
numbers = input().split()

numbers_list = [int(x) for x in numbers]
middle = len(numbers_list) // 2 + 1

left_time = 0
right_time = 0

for i in range(0, middle-1):
    time = numbers_list[i]
    left_time += time
    if time == 0:
        left_time *= 0.8

for j in range(len(numbers_list)-1, middle-1, -1):
    time = numbers_list[j]
    right_time += time
    if time == 0:
        right_time *= 0.8

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")



