employees = input().split()
employees_ints = list(map(int, employees))
factor = int(input())
employees_happiness = []

for emp in employees_ints:
    multiplied_int = emp * factor
    employees_happiness.append(multiplied_int)

sum_happiness = sum(employees_happiness)
employees_count = len(employees_ints)
average_happiness = sum_happiness / employees_count
happy_employees = [x for x in employees_happiness if x >= average_happiness]
happy_employees_count = len(happy_employees)

# print(employees_happiness)
# print(sum_happiness)
# print(employees_count)
# print(average_happiness)
# print(happy_employees)
# print(happy_employees_count)

if happy_employees_count >= employees_count / 2:
    print(f"Score: {happy_employees_count}/{employees_count}. Employees are happy!")

else:
    print(f"Score: {happy_employees_count}/{employees_count}. Employees are not happy!")






