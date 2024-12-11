l = [[2,3],[2,2],[2,3]]

def get_uninum(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

print(get_uninum(l))