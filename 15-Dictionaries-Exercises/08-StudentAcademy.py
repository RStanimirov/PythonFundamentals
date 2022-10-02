n = int(input())

student_dict = {}
average_grades_dict = {}
average_grade = 0

for i in range(0, n*2, 2):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_dict:
        student_dict[student_name] = [student_grade]
    else:
        student_dict[student_name].append(student_grade)


for key, value in student_dict.items():
    average_grade = sum(value) / len(value)
    average_grades_dict[key] = average_grade
    if average_grade < 4.50:
        average_grades_dict.pop(key)

# print(student_dict)
# print(average_grades_dict)

sorted_average_grades_dict = dict(sorted(average_grades_dict.items(), key=lambda x: -x[1]))

for key, value in sorted_average_grades_dict.items():
    print(f"{key} -> {value:.2f}")
