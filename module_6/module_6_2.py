class Vehicle:

    __COLORS = {            # Решил добавить в задачку разнообразия с цветами
        'black'  :  '\033[90m',
        'white'  :  '\033[97m',
        'green'  :  '\033[92m',
        'red'    :  '\033[91m',
        'yellow' :  '\033[93m',
        'blue'   :  '\033[94m',
        'pink'   :  '\033[95m'
    }

    def __init__(self, owner, __model, __horsepower, __color):
        self.owner = owner
        self.__model = __model
        self.__horsepower = __horsepower
        self. __color = __color

    def get_model(self):
        return f'Model: {self.__COLORS[self.__color]}{self.__model}\033[0m' # Перекрашивает нашу машину в цвет

    def get_horsepower(self):
        return f'Horsepower: {self.__horsepower}'

    def get_color(self):
        return f'Color: {self.__color}'

    def set_color(self, color: str):
        if color.lower() in self.__COLORS:
            self.__color = color.lower()
        else:
            print(f'Can\'t change color to {color}')

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_color()}\n{self.get_horsepower()}\nOwner: {self.owner}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

    # def __init__(self, owner, __model, __horsepower, __color):
    #     super().__init__(owner, __model, __horsepower, __color)

if __name__ == '__main__':

    chaser = Sedan('Jesse Pinkman', 'Chaser', 276, 'white')
    chaser.print_info()

    chaser.set_color('Orange')
    chaser.set_color('green')
    chaser.owner = 'Walter White'

    chaser.print_info()
