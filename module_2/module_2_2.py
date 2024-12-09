_st = int(input("First: "))
_nd = int(input("Second: "))
_rd = int(input("Third: "))

if _st == _nd and _st == _rd and _nd == _rd:
    print(3)
elif _st == _nd or _st == _rd or _nd == _rd:
    print(2)
else:
    print(0)