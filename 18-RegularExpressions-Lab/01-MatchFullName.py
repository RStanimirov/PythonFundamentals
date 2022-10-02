import re

names_input = input()
regex_seq = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches_found = re.findall(regex_seq, names_input)
print(*matches_found)
