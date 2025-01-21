data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def addition_data(structure):
    nums = 0

    for item in structure:
        if isinstance(item, str):
            nums += len(item)
        elif isinstance(item, int):
            nums += item
        elif isinstance(item, list):
            for lst in item:
                if isinstance(lst, int):
                    nums += lst
                elif isinstance(lst, str):
                    nums += len(lst)
                else:
                    nums = addition_data(nums)

        elif isinstance(item, dict):
            for key in item:
                value = item[key]
                for key in item:
                    value = item[key]
                    if isinstance(key, str):
                        nums += len(key)
                    if isinstance(value, int):
                        nums += value
                    elif isinstance(value, str):
                        nums += len(value)

        elif isinstance(item, set):
            for st in item:
                if isinstance(st, int):
                    nums += st
                elif isinstance(st, str):
                    nums += len(st)
                else:
                    nums = addition_data(nums)

        elif isinstance(item, tuple):
            for tup in item:
                if isinstance(tup, int):
                    nums += tup
                elif isinstance(tup, str):
                    nums += len(tup)
                else:
                    nums = addition_data(nums)
        else:
            continue
    return nums

print(addition_data(data_structure))
