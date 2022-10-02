import re

text = input()

regex_pattern = "\\b(\\d{2})([-.\\/])([A-Z][a-z]{2})\\2(\\d{4})\\b"
output_matches = re.findall(regex_pattern, text)

for x in output_matches:
    print(f"Day: {x[0]}, Month: {x[2]}, Year: {x[3]}")