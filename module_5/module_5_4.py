class House:
    # Module_5_4 "Class Attribute" ↓ #############
    houses_history = []

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        cls.houses_history.append(args[0])
        return inst

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} has been demolished, but it will remain in history!')

if __name__ == '__main__':
    google = House('Google', 20)
    print(House.houses_history)
    microsoft = House('Microsoft', 15)
    print(House.houses_history)
    yandex = House('Yandex', 10)
    print(House.houses_history)

    del microsoft
    del google

    print(House.houses_history)