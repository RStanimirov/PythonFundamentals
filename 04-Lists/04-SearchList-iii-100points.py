n = int(input())
search_word = input()
my_list = []
filtered_list = []

for i in range(0, n):
    input_sentence = input()
    my_list.append(input_sentence)
print(my_list)

for element in my_list:
    if search_word in element:
        filtered_list.append(element)
print(filtered_list)