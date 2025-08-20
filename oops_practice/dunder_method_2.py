import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # A good repr is always helpful!
        return f"Vector({self.x}, {self.y})"

    # Overloads the '+' operator
    def __add__(self, other):
        """
        This is called when you do vector1 + vector2.
        It should return a new Vector object.
        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # Overloads the len() function
    def __len__(self):
        """
        Called when you do len(vector).
        Returns the magnitude (length) of the vector.
        """
        # Using the Pythagorean theorem: a^2 + b^2 = c^2
        magnitude = math.sqrt(self.x**2 + self.y**2)
        return int(magnitude)

    # Overloads the '==' operator
    def __eq__(self, other):
        """Called when you do vector1 == vector2."""
        return self.x == other.x and self.y == other.y

# --- Let's test our new Vector powers! ---

v1 = Vector(2, 3)
v2 = Vector(5, 1)

# 1. Test addition using '+'
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

# 2. Test length using len()
v4 = Vector(3, 4) # A classic 3-4-5 triangle
print(f"The length of {v4} is {len(v4)}")

# 3. Test equality using '=='
v5 = Vector(2, 3)
print(f"Is {v1} equal to {v3}? {v1 == v3}")
print(f"Is {v1} equal to {v5}? {v1 == v5}")