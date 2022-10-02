numbers_str = input().split()
removing_factor = int(input())

for i in range(len(numbers_str)):
    numbers_str[i] = int(numbers_str[i])

for i in range(removing_factor):
    min_number = min(numbers_str)
    numbers_str.remove(min_number)

for i in range(len(numbers_str)):
    numbers_str[i] = str(numbers_str[i])

print(", ".join(numbers_str))
