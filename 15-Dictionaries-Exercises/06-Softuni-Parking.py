n = int(input())

register_dict = {}

for i in range(n):
    data = input().split()
    action = data[0]

    if action == "register":
        user = data[1]
        license = data[2]

        if user not in register_dict:
            register_dict[user] = license
            print(f"{user} registered {license} successfully")
        else:
            print(f"ERROR: already registered with plate number {license}")

    elif action == "unregister":
        user = data[1]

        if user not in register_dict:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            register_dict.pop(user)

for key, value in register_dict.items():
    print(f"{key} => {value}")