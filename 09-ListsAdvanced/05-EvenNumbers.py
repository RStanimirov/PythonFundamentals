input_list = input().split(', ')
input_list_int = list(map(int, input_list))

output_list = []

for i in range(len(input_list_int)):
    if input_list_int[i] % 2 == 0:
        output_list.append(i)

print(output_list)





