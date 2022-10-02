num_1 = int(input())
num_2 = int(input())

factorial_num_1 = 1
factorial_num_2 = 1

for i in range(1, num_1 + 1):
    factorial_num_1 *= i

for j in range(1, num_2 + 1):
    factorial_num_2 *= j

print(f"{factorial_num_1 / factorial_num_2:.2f}")


