n = int(input())
pos_counter = 0
neg_sum = 0
pos_list = []
neg_list = []

for i in range(0, n):
    input_int = int(input())

    if input_int >= 0:
        pos_counter += 1
        pos_list.append(input_int)
    elif input_int < 0:
        neg_sum += input_int
        neg_list.append(input_int)

print(pos_list)
print(neg_list)
print(f"Count of positives: {pos_counter}. Sum of negatives: {neg_sum}")

