random_number = int(input()) + 1

for i in range(0, len(str(random_number))):
    cheker = str(random_number).count(str(random_number)[i])

    while cheker > 1:
        random_number += 1
        cheker = str(random_number).count(str(random_number)[i])

print(random_number)