# n = int(input())
# total_sum = 0
#
# for i in range(0, n):
#     total_sum += ord(input())
#
# print(f'The sum equals: {total_sum}')

n = int(input())
total_sum = 0

for i in range(0, n):
    char = ord(input())
    total_sum += char

print(f'The sum equals: {total_sum}')