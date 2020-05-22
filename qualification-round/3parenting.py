import numpy

n_cases = int(input())

solutions = []
for _ in range(n_cases):
    minutes_C = []
    minutes_J = []

    activities = []

    n_activities = int(input())
    for i in range(n_activities):
        activity = [i]
        activity += [int(n) for n in input().split(" ")]
        activities.append(activity)

    # Sort activities by starting time.
    ord_activities = sorted(activities, key=lambda x: x[1])

    assignments = []
    for act in ord_activities:
        start_act = act[1]
        end_act = act[2]
        minutes_act = numpy.arange(start_act, end_act).tolist()

        # Check if C and J are free during the activity to assign.
        set0 = set(minutes_act)
        setC = set(minutes_C)
        setJ = set(minutes_J)
        free_C = not set0.intersection(setC)
        free_J = not set0.intersection(setJ)

        if free_C:
            minutes_C += minutes_act
            assignment = (act[0], act[1], act[2], 'C')
            assignments.append(assignment)
        elif free_J:
            minutes_J += minutes_act
            assignment = (act[0], act[1], act[2], 'J')
            assignments.append(assignment)
        else:
            assignment = (act[0], act[1], act[2], 'I')
            assignments.append(assignment)

    solution = ""
    impossible = False
    # Sort assignments by starting time.
    assignments.sort(key=lambda x: x[0])
    for ass in assignments:
        if ass[3] == 'I':
            impossible = True
        else:
            solution += ass[3]

    if not impossible:
        solutions.append(solution)
    else:
        solutions.append("IMPOSSIBLE")

for i, sol in enumerate(solutions):
    print("Case #{}: {}".format(i + 1, sol))



