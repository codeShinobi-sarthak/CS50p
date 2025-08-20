
"""
Here, the Car class doesn't know or care about the internal workings of the Engine. It simply holds an Engine object and tells it what to do. This is a very flexible design. If we later create a more advanced V8Engine or ElectricEngine, we could easily swap it in without having to change the Car class at all.

"""


# First, create the component class
class Engine:
    def start(self):
        print("Engine is running...")

    def stop(self):
        print("Engine has stopped.")

# Now, create the container class that USES the component
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # This is COMPOSITION: The Car 'has an' Engine object.
        self.engine = Engine()

    def start_car(self):
        print(f"Starting the {self.make} {self.model}...")
        # The Car class delegates the work to its Engine component.
        self.engine.start()

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()

# --- Using the composed class ---
my_car = Car("Ford", "Mustang")
my_car.start_car()
my_car.stop_car()