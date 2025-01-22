data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def addition_data(data, summa=0):

    for item in data:

        if isinstance(item, str):
            summa += len(item)
        elif isinstance(item, int):
            summa += item
        elif isinstance(item, list):

            for lst in item:
                if isinstance(lst, int):
                    summa += lst
                elif isinstance(lst, str):
                    summa += len(lst)
                else:
                    summa = addition_data([lst], summa)


        elif isinstance(item, dict):

            for key in item:
                value = item[key]

                if isinstance(key, str):
                    summa += len(key)
                if isinstance(value, int):
                    summa += value
                elif isinstance(value, str):
                    summa += len(value)

        elif isinstance(item, set):

            for st in item:

                if isinstance(st, int):
                    summa += st
                elif isinstance(st, str):
                    summa += len(st)
                else:
                    summa = addition_data([st], summa)

        elif isinstance(item, tuple):

            for tup in item:

                if isinstance(tup, int):
                    summa += tup
                elif isinstance(tup, str):
                    summa += len(tup)
                else:
                    summa = addition_data([tup], summa)
        else:
            continue

    return summa

print(addition_data(data_structure))
