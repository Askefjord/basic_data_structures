def get_matrix(line, column, value):
    matrix = []

    for i in range(line):
        a = []
        matrix.append(a)

        for j in range(column):
            a.append(value)
    return matrix

m = get_matrix(3,4,2)
print(m)