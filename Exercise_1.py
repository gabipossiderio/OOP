class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def height(self):
        return f'This is {self._name} height: {self._height} meters.'

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def age(self):
        return f'This is {self._name} age: {self._age} years.'

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def dados(self):
        return f'{self._name} has {self._age} years and {self._height} meters.'


user = Person('Jorginho', 4, 1.55)
user.age = 7
print(user.age)
