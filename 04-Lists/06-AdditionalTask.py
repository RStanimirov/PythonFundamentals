my_list = ['dog', 'cat']

my_element = my_list.index('dog')

for i in range(len(my_list[my_element])):
    if 'o' == my_list[my_element][i]:
        print(i)
