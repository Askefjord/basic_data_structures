num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
n_prime = []
x = 0
cnt = 0

for i in num:
    for j in range(1, i + 1):
        x = i % j
        if x == 0:
            cnt += 1
            if cnt == 2:
                prime.append(i)

            
            
        #else:
            #n_prime.append(i)
print(prime)
print(n_prime)