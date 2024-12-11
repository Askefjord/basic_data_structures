import random
pairs = []
result = []

def get_uninum(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

for i in range (1,21):
    for j in range(1,21):
        pairs.append([i,j])
pairs = get_uninum(pairs)
rn = random.randrange(3,21)
for i in pairs:
    if rn % sum(i):
        result.append(i)
print(result)
