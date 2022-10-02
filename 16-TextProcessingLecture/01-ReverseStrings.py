word = input()

while word != "end":
    mirror_word = ''
    for x in reversed(word):
        mirror_word += x
    print(f"{word} = {mirror_word}")

    word = input()


# text = input()
# while text != "end":
#     text_reversed = ""
#     for ch in reversed(text):
#         text_reversed += ch
#     print(text + " = " + text_reversed)
#     text = input()
