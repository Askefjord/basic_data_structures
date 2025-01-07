class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Module_5_2 "Dunder Methods" ↓ #############
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'\nName is: {self.name}\nNumber of floors: {self.number_of_floors}'
    #############################################

    def go_to(self, floor):
        if floor > self.number_of_floors:
            print('This floor does not exist')
        else:
            for num in range(1, floor+1):
                print(num)

some_moll = House('Some Moll', 15)
some_moll.go_to(17)
some_moll.go_to(5)

# ↓ Module_5_2 "Dunder Methods"
print(some_moll)
print(len(some_moll))