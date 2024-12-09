#Dicts
my_dict = {"Ruby": 1993, "C++": 1985, "Python": 1994}

print("Dict", my_dict)
print("Existing value", my_dict.get("Python"))
print("Not Existing value", my_dict.get("Java"))

my_dict["Java"] = 1996
my_dict["Assembler"] = 1947

print(my_dict.pop("C++"))
print(my_dict)

#Sets

my_set = {0.3, True, 2, "set", 2, True, False, 1.4}
print(my_set)
my_set.add(0.24)
my_set.add("frozenset")
my_set.discard(False)
print(my_set)