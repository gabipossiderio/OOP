class Person:

    def __init__(self, name, age, weight, height):
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height

    def increase_age(self, new_age):
        if new_age > self._age:
            for i in range(self._age, new_age):
                if i < 21:
                    self._height += 0.5
            self._age = new_age
        else:
            print('Please, enter an age greater than the current age.')

    def change_weight(self, new_weight):
        self._weight = new_weight

    def increase_height(self, new_height):
        self._height = new_height
