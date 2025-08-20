class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Information:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is starting.")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

    def honk(self):
        print("Beep! Beep! The car is honking.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike ):
        super().__init__(make, model, year)
        self.type_of_bike  = type_of_bike 

    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.type_of_bike}")

    def start_engine(self):
        print("vroom vroom! The motorcycle engine is starting.")

    def do_wheelie(self):
        print("The motorcycle is doing a wheelie!")


# Test the Car class
my_car = Car("Toyota", "Camry", 2022, 4)
my_car.display_info()
my_car.start_engine()
my_car.honk()

print("\n" + "-"*20 + "\n")

# Test the Motorcycle class
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2020, "Cruiser")
my_motorcycle.display_info() # This should use the parent's method
my_motorcycle.start_engine() # This should use the overridden method
my_motorcycle.do_wheelie()