class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

    def draw(self):
        print("Drawing a shape")

    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def draw(self):
        print("Drawing a square")

def describe_shape(shape):
    print("Shape description:")
    shape.draw()
    print(f"Area: {shape.area()}")



# --- Testing ---
# Create a list of different shape objects
shapes = [
    Circle(5),
    Square(4)
]

# Loop through the shapes and use the polymorphic function
print("--- Describing Shapes ---")
for shape in shapes:
    describe_shape(shape)
    print("-" * 15)