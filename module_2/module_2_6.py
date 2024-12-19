import random
rnum = random.randrange(3,21)
pairs = []
result = []
ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
nr = []
r = 0
while r < 18:
    for i in ran:
        for j in ran:
            pairs.append([i,j+1])
        ran.remove(i)
        r = i
        break

# for k in range(len(ran)):
#     for i in ran:
#         for j in ran:
#             if j not in nr:
#                 pairs.append([i,j+1])
#         nr.append(i)
#         break
# print(pairs)

for i in range(len(pairs)):
    if rnum % sum(pairs[i]) == 0:
        x = pairs[i]
        result.append(x)

# result = ''.join(str(num) for sublist in pairs for num in sublist)
result = sum(result, [])
print(f'Random number is: {rnum}')
print('Your code: ', *result)
