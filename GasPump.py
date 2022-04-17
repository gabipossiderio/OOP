class GasPump:

    def __init__(self, type_fuel, fuel_value, fuel_quantity):
        self._type_fuel = type_fuel
        self._fuel_value = fuel_value
        self._fuel_quantity = fuel_quantity

    def change_value(self, new_value):
        self._value = new_value

    def change_fuel(self, new_type):
        self._type_fuel = new_type

    def change_quantity(self, new_quantity):
        self._fuel_quantity = new_quantity

    def refill_value(self, value):
        fueled = value / self._fuel_value
        if fueled > self._fuel_quantity:
            old_fuel_quantity = self._fuel_quantity
            self._fuel_quantity = 0
            return old_fuel_quantity
        self._fuel_quantity -= fueled
        return fueled

    def refill_liter(self, liter_quantity):
        fueled = liter_quantity * self._fuel_value
        if liter_quantity > self._fuel_quantity:
            old_fuel_quantity = self._fuel_quantity
            self._fuel_quantity = 0
            return old_fuel_quantity * self._fuel_value
        self._fuel_quantity -= liter_quantity
        return fueled


v1 = GasPump('Álcool', 7, 50)
print(Abastece.refill_value(60))
print(vars(Abastece))
