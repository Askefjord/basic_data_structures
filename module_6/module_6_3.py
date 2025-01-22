from random import randrange


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords=None):
        if _cords is None:
            self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, x, y, z):
        self._cords[0] = x * self.speed
        self._cords[1] = y * self.speed

        if z < 0:
            print('It\'s too deep, I can\'t dive :(')
        else:
            self._cords[2] = z * self.speed

    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print('Be careful, I\'m attacking you 0_o')
        else:
            print('Sorry, I\'m peaceful :)')

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        rand_eggs = randrange(1, 5)
        print(f'Here are {rand_eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, z):
        self._cords[2] -= abs(z) * (self.speed // 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'


if __name__ == '__main__':
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()
