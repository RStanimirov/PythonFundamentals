str_one = input()
str_two = input()

new_word = ""

for i in range(1, len(str_one) + 1):
    a_letter = ord(str_one[i - 1])
    b_letter = ord(str_two[i - 1])

    if a_letter != b_letter:
        new_word = str_two[:i] + str_one[i:]
        print(new_word)
