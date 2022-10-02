task = input()
to_do_list = []
while task != 'End':
    to_do_list.append(task)
    task = input()

to_do_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
print([x.split('-')[1] for x in to_do_list])

