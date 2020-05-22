n_test = int(input())
solutions = []

for _ in range(n_test):
    _ = int(input())
    input_data = []

    for i in range(10000):
        _, response = input().split(" ")
        input_data.append(response)

    letters = "".join([x for x in input_data])
    set_letters = set(letters)

    first_letters = [x[0] for x in input_data]
    set_first_letters = set(first_letters)

    occ = []
    for letter in set_first_letters:
        occ.append((letter, first_letters.count(letter)))

    occ.sort(key=lambda x: x[1], reverse=True)

    missing_letter = list(set_first_letters.symmetric_difference(set_letters))[0]

    server_str = [
        missing_letter,
        occ[0][0],
        occ[1][0],
        occ[2][0],
        occ[3][0],
        occ[4][0],
        occ[5][0],
        occ[6][0],
        occ[7][0],
        occ[8][0]
    ]

    solutions.append("".join(server_str))

for i, sol in enumerate(solutions):
    print("Case #{}: {} ".format(i + 1, sol))
