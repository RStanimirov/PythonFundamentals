gifts = input().split(" ")
command = [0, 1]

while command[0] != "No" and command[1] != "Money":
    if command[0] == "OutOfStock":
        for i in range(0, len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = None
    if command[0] == "Required":
        req_gift = command[1]
        idx = int(command[2])
        if -1 < idx < len(gifts):
            gifts[idx] = req_gift
    if command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(" ")

final_list = []
for c in range(0, len(gifts)):
    if gifts[c] is not None:
        final_list.append(gifts[c])

final_list = " ".join(final_list)
print(final_list)