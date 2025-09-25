# We continue in the same file car.py from the previous lesson.
# In this lesson, we add Methods to the Car class.
# Methods are functions defined inside a class.

# (1) DEFINE THE CAR CLASS WITH ATTRIBUTES AND A METHOD
class Car:
    # (1-1) CLASS ATTRIBUTE
    wheels = 4

    # (1-2) INSTANCE ATTRIBUTES
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # (1-3) METHOD INSIDE CLASS
    def description(self):
        return f"{self.brand} car, {self.color}, with {self.wheels} wheels."

# (2-1) CREATE FIRST OBJECT
car1 = Car("Tesla", "Red")

# (2-2) CALL METHOD ON FIRST OBJECT
print(car1.description())

# (3-1) CREATE SECOND OBJECT
car2 = Car("BMW", "Blue")

# (3-2) CALL METHOD ON SECOND OBJECT
print(car2.description())
