import re

text = input().lower()
search_word = input().lower()
words_list = []
search_word_list = []

pattern = rf"\b{search_word}\b"
words = re.finditer(pattern, text)

for x in words:
    words_list.append(x.group())

for y in words_list:
    if y == search_word:
        search_word_list.append(search_word)

print(len(search_word_list))