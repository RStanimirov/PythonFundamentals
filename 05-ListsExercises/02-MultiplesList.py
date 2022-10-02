n_factor = int(input())
n_sequence = int(input())
my_list = []
next_num = 0

for i in range(n_sequence):
    next_num += n_factor
    my_list.append(next_num)

print(my_list)