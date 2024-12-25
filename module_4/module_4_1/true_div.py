import math

def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return math.inf