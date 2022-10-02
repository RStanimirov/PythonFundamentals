def repeat_str(string, n):
    repeated_string = string * n
    return repeated_string

str = input()
factor = int(input())

print(repeat_str(str, factor))
