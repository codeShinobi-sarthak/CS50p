from abc import ABC, abstractmethod
import math

# --- The Abstract Base Class (The Contract) ---
class Shape(ABC):
    """
    This is an abstract class that defines the contract for all shapes.
    Any class inheriting from Shape `MUST` implement draw() and area().
    """
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

# --- Concrete Child Classes (Fulfilling the Contract) ---
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # We provide the required 'draw' method
    def draw(self):
        print("Drawing a circle.")

    # We provide the required 'area' method
    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    # We provide the required 'draw' method
    def draw(self):
        print("Drawing a square.")

    # We provide the required 'area' method
    def area(self):
        return self.side_length ** 2

# --- Using the Concrete Classes ---
# This now works perfectly because the contract is fulfilled.
shapes = [
    Circle(10),
    Square(5)
]

# Our polymorphic loop works just like before, but now with a guarantee.
# We are certain that every object in this list has .draw() and .area() methods.
for shape in shapes:
    shape.draw()
    print(f"Area: {shape.area()}")
    print("-" * 15)