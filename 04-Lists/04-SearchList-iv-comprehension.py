n = int(input())
search_word = input()
my_list = []

for i in range(0, n):
    input_sentence = input()
    my_list.append(input_sentence)
print(my_list)
# below is an example of using a comprehension list
filtered_list = [i for i in my_list if search_word in i]
print(filtered_list)