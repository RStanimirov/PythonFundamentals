#Lecturers' a bit clumsy solution:
import re

text = input()

pattern = r"(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"
pattern_numbers = r"\d"
threshold = 1
emoji_count = 0
emojis_to_print = []

all_numbers_in_text_as_strings = re.findall(pattern_numbers, text)
all_numbers_as_integers = [int(x) for x in all_numbers_in_text_as_strings]
emoji_matches = re.finditer(pattern, text)

for x in all_numbers_as_integers:
    threshold *= x

for match in emoji_matches:
    emoji_count += 1
    data = match.groupdict()
    emoji = data["emoji"]
    emoji_coolness = sum([ord(x) for x in emoji])

    if emoji_coolness >= threshold:
        emojis_to_print.append(f"{data['surr']}{data['emoji']}{data['surr']}")

print(f"Cool threshold: {threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
# print("\n".join(emojis_to_print))
for emoji in emojis_to_print:
    print(emoji)