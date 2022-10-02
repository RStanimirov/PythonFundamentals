input_words = input().split()

char_code_str = ''
new_word = []

deciphered_words = []

for item in input_words:

    for char in item:
        if char.isnumeric():
            char_code_str += char
        else:
            new_word.append(char)

    char_at_beginning = chr(int(char_code_str))
    new_word.insert(0, char_at_beginning)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = "".join(new_word)
deciphered_words.append(new_word)

print(" ".join(deciphered_words))