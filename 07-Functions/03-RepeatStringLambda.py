string = input()
n = int(input())

repeat_str = lambda a, b: a * b
result = repeat_str(string, n)

print(result)