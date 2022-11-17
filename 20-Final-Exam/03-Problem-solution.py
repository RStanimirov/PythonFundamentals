command = input()
followers_dict = {}

while command != "Log out":
    data = command.split(': ')
    action = data[0]

    if action == "New follower":
        username = data[1]
        if username not in followers_dict:
            followers_dict[username] = [0, 0]

    elif action == "Like":
        username = data[1]
        likes_count = int(data[2])
        if username not in followers_dict:
            followers_dict[username] = [likes_count, 0]
        else:
            followers_dict[username][0] += likes_count

    elif action == "Comment":
        username = data[1]
        if username not in followers_dict:
            followers_dict[username] = [0, 1]
        else:
            followers_dict[username][1] += 1

    elif action == "Blocked":
        username = data[1]
        if username not in followers_dict:
            print(f"{username} doesn't exist.")
        else:
            del followers_dict[username]

    command = input()

# print(followers_dict)
print(f"{len(followers_dict)} followers")

for key, value in sorted(followers_dict.items(), key=lambda x: (-sum(x[1]), x[0])):
    print(f"{key}: {sum(value)}")