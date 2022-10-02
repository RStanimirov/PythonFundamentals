def check_chain(x, y):
    if field[x][y] and not visited[x][y]:
        visited[x][y] = True
        return check_chain(x - 1, y) + check_chain(x, y + 1) + check_chain(x + 1, y) + check_chain(x, y - 1) + 1
    else:
        return 0


rows, field, points, visited, max_length = int(input()), [], [], [], 0

# import data and set an empty frame around matrix
for i in range(rows):
    tempo = ('- ' + input() + ' -').split(' ')
    morph = [1 if x == '.' else 0 for x in tempo]
    field.append(morph)
field.append([0] * len(field[0]))
field.insert(0, [0] * len(field[0]))

# identify all starting dots
for i in range(1, len(field) - 1):
    for j in range(1, len(field[0]) - 1):
        if field[i][j]:
            points.append([i, j])

# create another matrix, mirroring dimensions of the field - to be used for marking visited
for row in range(len(field)):
    tempo = []
    for col in range(len(field[0])):
        tempo.append(False)
    visited.append(tempo)

# iterating over the starting dots, to explore chain lengths and getting max length
for p in points:
    current_chain_length = check_chain(p[0], p[1])
    if current_chain_length > max_length:
        max_length = current_chain_length
print(max_length)