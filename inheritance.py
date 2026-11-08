class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_car_info(self):
        self.display_info()
        print(f"Doors: {self.doors}")

if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 4)
    my_car.display_car_info()
