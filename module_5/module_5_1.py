class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor > self.number_of_floors:
            print('This floor does not exist')
        else:
            for num in range(1, floor + 1):
                print(num)

    # Module_5_2 "Dunder Methods" ↓ #############
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name is: {self.name} Number of floors: {self.number_of_floors}'
    #############################################

    # Module_5_3 "Overdrive Methods" ↓ ##########
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            return House(f'{self.name} + {other.name}', self.number_of_floors + other.number_of_floors)
        else:
            return House(f'{self.name}', self.number_of_floors + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)
    #############################################

if __name__ == '__main__':

    some_moll = House('Some Moll', 15)
    aquapark = House('Aquapark', 10)

    some_moll.go_to(17)
    some_moll.go_to(5)

    # ↓ Module_5_2 "Dunder Methods"
    print('\n↓ Module_5_2 "Dunder Methods"')
    print(some_moll)
    print(len(some_moll))

    # ↓ Module_5_3 "Overdrive Methods"
    print('\n↓ Module_5_3 "Overdrive Methods"')
    some_moll.number_of_floors = 10
    aquapark.number_of_floors = 20

    print(some_moll)
    print(aquapark)

    print(some_moll == aquapark)

    some_moll = some_moll + 10
    print(some_moll)
    print(some_moll == aquapark)

    some_moll += 10
    print(some_moll)

    aquapark = 10 + aquapark
    print(aquapark)

    print(some_moll > aquapark)
    print(some_moll >= aquapark)
    print(some_moll < aquapark)
    print(some_moll <= aquapark)
    print(some_moll != aquapark)



