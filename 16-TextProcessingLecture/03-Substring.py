string_fragment = input()
text = input()

while string_fragment in text:
    text = text.replace(string_fragment, '')

print(text)