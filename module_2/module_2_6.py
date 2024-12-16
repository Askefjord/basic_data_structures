import random
rn = random.randrange(3,21)
pairs = []
result = []
ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
r = 0
while r < 18:
    for i in ran:
        for j in ran:
            pairs.append([i,j+1])
        ran.remove(i)
        r = i
        break

for i in pairs:
    if rn % sum(i) == 0:
        result.append(i)
print(rn)
print(result)
