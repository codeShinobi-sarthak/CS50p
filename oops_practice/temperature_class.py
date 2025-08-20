class Temperature:
    """
    A class that stores temperature in Celsius and allows
    access and modification in both Celsius and Fahrenheit.
    """
    _ABSOLUTE_ZERO_C = -273.15

    def __init__(self, celsius=0):
        # We use the public property 'celsius' here, not the private one.
        # This ensures our validation logic in the setter is run
        # when the object is first created.
        self.celsius = celsius

    @property
    def celsius(self):
        """The getter for the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """The setter for the temperature in Celsius."""
        if value < self._ABSOLUTE_ZERO_C:
            raise ValueError(f"Temperature cannot be below {self._ABSOLUTE_ZERO_C}°C.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """The getter for fahrenheit, calculated from Celsius."""
        # This value is calculated on-the-fly each time it's accessed.
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """The setter for fahrenheit, which converts and sets Celsius."""
        # This setter calculates the Celsius equivalent and then
        # re-uses the celsius setter's logic and validation.
        self.celsius = (value - 32) * 5/9


# Create a temperature object
temp = Temperature(10)

# Get the temperature in both scales
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

# Set the temperature using the fahrenheit property
print("\nSetting temperature to 68°F...")
temp.fahrenheit = 68

# Check the values again (celsius should have updated)
print(f"New Celsius: {temp.celsius}°C")
print(f"New Fahrenheit: {temp.fahrenheit}°F")

# Try to set an invalid temperature
try:
    print("\nTrying to set temperature below absolute zero...")
    temp.celsius = -300
except ValueError as e:
    print(f"Caught an error: {e}")