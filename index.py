class Flight():
    def __init__ (self, capacity, passenger):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        # self.passanger.append(name)
        if self.open_seat() == 0:
            return False
        self.passanger.append(name)
        return True

     
    def open_seat(self):
      return self.capacity == len(self, passenger=[])

passangers = ["Ron", "Harry", "Potter", "Matthew"]
airpeace=Flight(5)
nigerian_airways = Flight(3)


for person in passangers:
    if nigerian_airways.add_passaagers(person):
        print(f"Added{person}")
    else:
        print(f"GO BACK {person}!!!, seats are all full ")



        