people_n = int(input())
capacity_p = int(input())

full_course = people_n // capacity_p
remainder = people_n % capacity_p

if remainder == 0:
    print(full_course)
else:
    print(full_course + 1)
