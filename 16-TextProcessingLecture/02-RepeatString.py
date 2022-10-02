input_string = input().split()

for x in input_string:
    sub_string = x
    print(sub_string * len(sub_string), end='')