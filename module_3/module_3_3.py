def print_params(a=1, b='stroka', c=True):
    print(a, b, c)

#print_params(2,3,4,2) #TypeError
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [0.2, 'sky', ['a','b']]
values_dict = {'a': 0, 'b': False, 'c': 'wind'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [(2.3, 'dont use this'), 404]
print_params(False, *values_list2)