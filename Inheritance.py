class Equipment:

    def __init__(self, screen_size, screen_type):
        self._screen_size = screen_size
        self.screen_type = screen_type

    @property
    def screen_size(self):
        return self._screen_size

    @property
    def screen_type(self):
        return self._screen_type

    @screen_size.setter
    def screen_size(self, new_screen_size):
        self._screen_size = new_screen_size

    @screen_type.setter
    def screen_type(self, new_screen_type):
        self._screen_type = new_screen_type

    def display(self):
        return f'{self._screen_size}, {self._screen_type}'


class Computer(Equipment):

    def __init__(self, screen_size, screen_type, keyboard_type, memory_capacity):
        super().__init__(screen_size, screen_type)
        self._keyboard_type = keyboard_type
        self._memory_capacity = memory_capacity

    @property
    def keyboard_type(self):
        return self._keyboard_type

    @property
    def memory_capacity(self):
        return self._memory_capacity

    @keyboard_type.setter
    def keyboard_type(self, new_keyboard_type):
        self._keyboard_type = new_keyboard_type

    @memory_capacity.setter
    def memory_capacity(self, new_memory_capacity):
        self._memory_capacity = new_memory_capacity

    def display(self):
        equipment = super().display()
        return f'{equipment}, {self._keyboard_type}, {self._memory_capacity}'


class EquipmentTest:

    @staticmethod
    def main():
        notebook = Equipment(15.6, 'LED')
        cpu = Computer(24, 'LED', 'Mechanical', 16)
        return notebook, cpu


meus_equipamentos = EquipmentTest()
equipamento1, equipamento2 = meus_equipamentos.main()
print(equipamento1.display())
print(equipamento2.display())
