import re

text = input()

regex_pattern = r"(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b"
output_matches = re.findall(regex_pattern, text)

print(", ".join(output_matches))