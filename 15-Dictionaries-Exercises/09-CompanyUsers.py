# RS solutionJul 2021
commmand = input()

company_dict = {}

while commmand != "End":
    data = commmand.split(" -> ")
    company = data[0]
    employee = data[1]

    if company not in company_dict:
        company_dict[company] = []

    if employee not in company_dict[company]:
        company_dict[company].append(employee)

    commmand = input()

sorted_dict = dict(sorted(company_dict.items(), key=lambda x: x[0]))

for key, value in sorted_dict.items():
    print(f"{key}")
    for v in value:
        print(f"-- {''.join(v)}")