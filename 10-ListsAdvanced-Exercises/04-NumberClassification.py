input_list = input().split(', ')
input_ints = list(map(int, input_list))
positive = []
negative = []
even = []
odd = []

for num in input_ints:
    if num >= 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)

positive_str = ", ".join(str(x) for x in positive)
negative_str = ", ".join(str(x) for x in negative)
even_str = ", ".join(str(x) for x in even)
odd_str = ", ".join(str(x) for x in odd)

print(f"Positive: {positive_str}")
print(f"Negative: {negative_str}")
print(f"Even: {even_str}")
print(f"Odd: {odd_str}")