def get_matrix(line, column, value):
    matrix = []

    for i in range(line):
        a = []
        matrix.append(a)

        for j in range(column):
            a.append(value)
    return matrix

m1 = get_matrix(3,1,0)
m2 = get_matrix(3,1,1)
m3 = get_matrix(3,1,0)
print(f'{m1}\n{m2}\n{m3}')