# duma = input()
# duma_reverse = ''
#
# for i in range(len(duma)-1, -1, -1):
#     duma_reverse += duma[i]
# print(duma_reverse)

# word = input()
# for i in range(len(word)-1, -1, -1):
#     print(word[i], end='')

# word = input()
# new_word = ''
# for letter in word:
#     new_word = letter + new_word
# print(new_word)

number = int(input())
for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range (number-1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()



