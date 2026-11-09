class Battery():
    def __init__(self, battery_percentage=100):
        self.battery_percentage = battery_percentage


    def show_battery_percentage(self):
        print("This battery has {self.battery_percentage} charge ")
        


class Vehicle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.model = color



class Tricycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.wheels = 3

    def introduction(self):
        print(f"This is a {self, self.brand}, ")