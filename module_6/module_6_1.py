class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'The {self.name} ate {food.name}')
        else:
            print(f'The {self.name} didn\'t eat {food.name}')

class Plant:
    edible = None # Да, я решил отойти от условий задачи, ведь так будет логичнее относительно объектов

    def __init__(self, name):
        self.name = name

class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):

    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = True

class Flower(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = False

if __name__ == '__main__':
    wolf = Predator('Wolf')
    horse = Mammal('Horse')
    rose = Flower('Rose')
    grape = Fruit('Grape')

    print(wolf.name)
    print(rose.name)

    print(wolf.alive)
    print(horse.fed)

    wolf.eat(rose)
    horse.eat(grape)

    print(wolf.alive)
    print(horse.fed)