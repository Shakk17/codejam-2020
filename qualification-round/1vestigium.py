def get_trace(matrix):
    size = len(matrix[0])
    sum = 0
    for i in range(size):
        sum += matrix[i][i]
    return sum


def get_n_repeated_rows(matrix):
    count = 0
    n_rows = len(matrix)
    for row in range(n_rows):
        if len(set(matrix[row])) != len(matrix[row]):
            count += 1
    return count


def get_n_repeated_cols(matrix):
    trans_matrix = [list(x) for x in zip(*matrix)]
    return get_n_repeated_rows(trans_matrix)


def get_matrix(size):
    matrix = []
    for row in range(size):
        elements = input().split(" ")
        matrix.append([int(element) for element in elements])
    return matrix


n_matrix = int(input())

matrixes = []
solutions = []
for i in range(n_matrix):
    size = int(input())
    matrix = get_matrix(size)
    matrixes.append(matrix)
    trace = get_trace(matrix)
    repeated_rows = get_n_repeated_rows(matrix)
    repeated_cols = get_n_repeated_cols(matrix)
    solutions.append((trace, repeated_rows, repeated_cols))

for i, sol in enumerate(solutions):
    print("Case #{}: {} {} {}".format(i + 1, sol[0], sol[1], sol[2]))
