text = input().split()

text_as_str = "".join(text)
diction = {}

for x in text_as_str:
    if x not in diction:
        diction[x] = 0
    diction[x] += 1

for key, value in diction.items():
    print(f"{key} -> {value}")
