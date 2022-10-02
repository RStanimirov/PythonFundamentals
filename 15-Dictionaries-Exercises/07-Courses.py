# (RS solution Jul 2021)

command = input()

courses_dict = {}

while command != "end":
    data = command.split(" : ")
    course = data[0]
    username = data[1]

    if course not in courses_dict:
        courses_dict[course] = [username]
    else:
        courses_dict[course].append(username)

    command = input()

sorted_dict = dict(sorted(courses_dict.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in sorted_dict.items():
    print(f"{key}: {len(value)}")
    for v in sorted(value):
        print(f"-- {''.join(v)}")