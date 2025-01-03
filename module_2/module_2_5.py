import random

def get_matrix(line, column):
    matrix = []

    for i in range(line):
        a = []
        matrix.append(a)

        for j in range(column):
            rn = random.randrange(0, 2)
            a.append(rn)
    return matrix


m1 = sum(get_matrix(6,1), [])
m2 = sum(get_matrix(6,1), [])
m3 = sum(get_matrix(6,1), [])
m4 = sum(get_matrix(6,1), [])
m5 = sum(get_matrix(6,1), [])
m6 = sum(get_matrix(6,1), [])
print(f'{m1}\n{m2}\n{m3}\n{m4}\n{m5}\n{m6}')