import random
rn = random.randrange(3,21)
pairs = []
result = []

def get_uninum(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

for i in range (1,20):
    for j in range(1,20):
        pairs.append([i,j])
pairs = get_uninum(pairs)

for i in pairs:
    if rn % sum(i) == 0:
        result.append(i)
print(rn)
print(result)
