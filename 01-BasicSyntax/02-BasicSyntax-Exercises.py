word = input()
word_repeated = ''

for i in range (0, len(word), 1):
    word_repeated = word[i] + word[i]
    print(word_repeated, end='')

