def multi_digits(number):
    strnum = str(number)
    if len(strnum) == 1:
        return
    return int(strnum[:1]) * multi_digits(int(strnum[1:]))

print(multi_digits(323))