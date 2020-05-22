def distance(x, x_goal):
    return abs(x - x_goal)


solutions = []

for test in range(int(input())):
    position = [0, 0]
    x_goal, y_goal = map(int, input().split(" "))
    goal = [x_goal, y_goal]
    if (x_goal + y_goal) % 2 == 0:
        solutions.append("IMPOSSIBLE")
    else:
        somma = abs(x_goal) + abs(y_goal)
        # Trova potenza di 2 max che sia minore di somma.
        i_max = []
        i = 0
        continua = 1
        while continua:
            i_max.append(2 ** i)
            i += 1
            continua = 2 ** i < somma

        action = list()
        distances = [distance(position[0], x_goal), distance(position[1], y_goal)]
        while distances != [0, 0]:
            # Scelgo il più lontano.
            chosen = 0
            if distances[1] > distances[0]:
                chosen = 1

            if goal[chosen] > position[chosen]:
                position[chosen] += i_max[-1]
                if chosen == 0:
                    action.append('E')
                else:
                    action.append('N')
            else:
                position[chosen] -= i_max[-1]
                if chosen == 0:
                    action.append('W')
                else:
                    action.append('S')
            i_max = i_max[:-1]
            distances = [distance(position[0], x_goal), distance(position[1], y_goal)]
        action.reverse()
        solutions.append("".join(action))

for i, sol in enumerate(solutions):
    print("Case #{}: {} ".format(i + 1, sol))
