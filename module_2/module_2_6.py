import random
rn = random.randrange(3,21)
pairs = []
result = []

def get_uninum(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)

    for i in range(len(numbers)):
        for j in range(len(unique)):
            if numbers[i][1] == unique[j]:
                break

    return unique


ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in list(ran):
    for j in range(2,20):
        pairs.append([i,j])
    ran.remove(i)

for i in pairs:
    if rn % sum(i) == 0:
        result.append(i)
print(rn)
print(result)
