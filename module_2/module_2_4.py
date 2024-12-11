num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
n_prime = []

for i in num:
    is_prime = True
    if i < 2:
        is_prime = False
        continue

    for j in range(2, int(i**0.5)+1):
       if i % j == 0:
           is_prime = False
           break
    if is_prime:
        prime.append(i)
    else:
        n_prime.append(i)

print(prime)
print(n_prime)
