import re

text = input()

pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(pattern, text)
cool_emojis = []
cool_threshold = 1

for x in text:
    if x.isdigit():
        cool_threshold *= int(x)

for y in matches:
    coolness_strength = 0
    for z in y[1]:
        coolness_strength += ord(z)

    if coolness_strength > cool_threshold:
        cool_emojis.append(y)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    print(''.join(emoji))
