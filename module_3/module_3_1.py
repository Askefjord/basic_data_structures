count_ = 0
def count_calls():
    global count_
    return count_

def string_info(string: str):
    global count_
    count_ += 1
    tuple_info = (len(string), string.upper(), string.lower())
    return tuple_info

def is_contains(string: str, list_to_search: list) -> bool:
    global count_
    count_ += 1
    for element in list_to_search:
        if type(element) == str:
            if element.lower() == string.lower():
                return True
            break
    return False

print(string_info('owergrowth'))
print(is_contains('flore', [True, 0.2, 'FloRE', 'Sunday']))
print(count_calls())
