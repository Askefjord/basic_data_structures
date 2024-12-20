import random
rnum = random.randrange(3,21)
result = []
plist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def get_unipairs(pairlist):
    pairs = list(pairlist)
    upairs = []
    r = 0
    l = len(pairlist)
    while r < l:
        for i in pairs:
            for j in pairs:
                upairs.append([i,j+1])
            pairs.remove(i)
            r = i
            break
    return upairs

unipairs = get_unipairs(plist)
for i in range(len(unipairs)):
    if rnum % sum(unipairs[i]) == 0:
        x = unipairs[i]
        result.append(x)

result = sum(result, [])
print(f'Random number is: {rnum}')
print('Your code: ', *result)
