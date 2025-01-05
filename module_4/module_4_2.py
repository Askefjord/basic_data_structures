def test_func():
    def inner_func():
       print('Я в области видимости функции test_function')
    inner_func()

# inner_func() <# Интерпритатор Python не обнаружил функцию
                # в global и built-in пространтсвах

test_func()