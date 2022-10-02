# text = input()
#
# vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
#
# for i in text:
#     if i not in vowels:
#         text = ''.join(i)
#
#         print(text, end='')

# # Another solution:
# text = input()
# vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
# no_vowels = ''.join([x for x in text if x not in vowels])
# print(no_vowels)

text_input = input()

no_vowels_list = []
no_vowels_str = ''
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

for i in text_input:
    if i not in vowels:
        no_vowels_list.append(i)

no_vowels_str = ''.join([x for x in no_vowels_list])
print(no_vowels_str)

