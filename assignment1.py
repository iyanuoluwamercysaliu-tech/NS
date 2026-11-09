class Phone:
    def __init__(self, brand, model, volume):
        self.brand = brand
        self.model = model
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def increase_volume(self, amount):
        if amount < 0:
            print("Cannot increase volume by a negative amount")
        elif self.__volume + amount > 100:
            print("Cannot increase volume beyond 100")
        else:
            self.__volume += amount

    def decrease_volume(self, amount):
        if amount < 0:
            print("Cannot decrease volume by a negative amount")
        elif self.__volume - amount < 0:
            print("Cannot decrease volume below 0")
        else:
            self.__volume -= amount


my_phone = Phone("Samsung", "S24", 70)
print(my_phone.get_volume())
my_phone.increase_volume(20)
print(my_phone.get_volume())
my_phone.increase_volume(20)
print(my_phone.get_volume())
my_phone.decrease_volume(30)
print(my_phone.get_volume())
my_phone.decrease_volume(100)
print(my_phone.get_volume())


