def move(x, y, char):
    if char == 'N':
        return x, y+1
    elif char == 'S':
        return x, y-1
    elif char == 'E':
        return x+1, y
    elif char == 'W':
        return x-1, y


solutions = []
n_test = int(input())

for _ in range(n_test):
    x, y, path = input().split(" ")
    x = int(x)
    y = int(y)
    path = list(path)

    path_positions = [(x, y)]
    distance = [(0, x + y)]
    for i, char in enumerate(path):
        pos = move(x, y, char)
        path_positions.append(pos)
        x, y = pos
        distance.append((i + 1, abs(x) + abs(y)))

    valid_dist = list(filter(lambda x: x[1] <= x[0], distance))
    valid_dist.sort(key=lambda x: x[0])
    if len(valid_dist) == 0:
        solutions.append("IMPOSSIBLE")
    else:
        solutions.append(valid_dist[0][0])


for i, sol in enumerate(solutions):
    print("Case #{}: {} ".format(i + 1, sol))
