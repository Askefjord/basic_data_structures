def multi_digits(number):
    strnum = str(number).rstrip('0')

    if len(strnum) > 1:
        return int(strnum[:1]) * multi_digits(int(strnum[1:]))
    else:
        return int(strnum[:1])

print(multi_digits(402030))
print(multi_digits(40203))
print(multi_digits(14202340))