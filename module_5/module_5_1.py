class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor > self.number_of_floors:
            print('This floor does not exist') 
        else:
            for num in range(1, floor+1):
                print(num)

some_moll = House('Some Moll', 15)
some_moll.go_to(17)
some_moll.go_to(5)