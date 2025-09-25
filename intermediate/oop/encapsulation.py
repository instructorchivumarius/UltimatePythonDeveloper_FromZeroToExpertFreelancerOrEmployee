# Getters and Setters
# In this lesson we use getters and setters to access and update private data safely.

# (1) DEFINE CLASS VEHICLE
class Vehicle:
    # (1-1) PRIVATE ATTRIBUTE
    __engine_number = "ENG-12345"

    # (1-2) GETTER METHOD
    def get_engine_number(self):
        return self.__engine_number

    # (1-3) SETTER METHOD
    def set_engine_number(self, new_number):
        self.__engine_number = new_number


# (2) CREATE OBJECT
car = Vehicle()

# (3) USE GETTER
print("Engine number:", car.get_engine_number())

# (4) USE SETTER
car.set_engine_number("ENG-98765")

# (5) USE GETTER AGAIN
print("Updated engine number:", car.get_engine_number())
