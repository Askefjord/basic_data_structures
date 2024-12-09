immutable_var = 12, 'immutable', 0.25, True
print(immutable_var)
#immutable_var[0] = 5 <-- Данная операция невозможна так как кортеж
#                         является неизменяемым типом данных, поэтоу
#                         изменение или добавление данных в него невозможно

mutable_list = ['global', 18, 0.3]
mutable_list[1] = 25
mutable_list.append(True)
print(mutable_list)
