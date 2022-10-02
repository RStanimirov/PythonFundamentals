username_list = input().split(', ')

valid_usernames_list = []
is_valid = False

for x in username_list:
    if len(x) < 3 or len(x) > 16:
        is_valid = False
    elif not x.isalnum() and '-' not in x and '_' not in x:
        is_valid = False
    else:
        is_valid = True
        valid_usernames_list.append(x)

print('\n'.join(valid_usernames_list))