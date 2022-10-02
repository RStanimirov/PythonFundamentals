n = int(input())
word = input()
new_list = []

for i in range(n):
    new_word = input()
    new_list.append(new_word)
print(new_list)

for j in new_list:
    while word in j:
        new_list.remove(j)
print(new_list)
