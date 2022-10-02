input_list = input().split()
output_list = []

for word in input_list:
    if len(word) % 2 == 0:
        output_list.append(word)

# output_words = ' '.join(str(x) for x in output_list)

for i in range(len(output_list)):
    print(output_list[i])




