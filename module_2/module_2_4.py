num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
n_prime = []

for i in num:
    for j in range(1, i):
        if i % j == 0 and i == j:
            prime.append(i)
        else:
            n_prime.append(i)
print(prime)
print(n_prime)