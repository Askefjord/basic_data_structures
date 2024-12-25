def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return 'Error: Division by zero!'