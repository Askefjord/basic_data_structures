class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, x, y, z):
        pass

class Bird(Animal):
    pass

class AquaticAnimal(Animal):
    pass

class PoisonousAnimal(Animal):
    pass

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird, Animal):
    pass
