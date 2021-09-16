class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def max_capacity(self):
        print('Gas tank capacity is {self.gas_tank_size}')
        return self.gas_tank_size

    def drive(self):
        print(f'The {self.model} is now driving.')