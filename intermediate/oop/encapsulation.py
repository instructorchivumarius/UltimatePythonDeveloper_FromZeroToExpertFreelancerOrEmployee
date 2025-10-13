# [1] Encapsulation 
#     In this lesson we learn how encapsulation hides data inside a class.
#
# [2] Private and Protected Variables
#     We continue in the same file encapsulation.py from the previous lesson.
#     In this lesson, we focus on access levels:
#       • Protected attributes → start with one underscore: _name
#       • Private attributes   → start with two underscores: __name (name-mangling)
#     We keep previous code and add safe access examples.
#____________________________________________________________________________________________


# [1]-1 DEFINE BASE CLASS VEHICLE
class Vehicle:
    # [1]-1-1 PUBLIC ATTRIBUTE
    brand = "Generic Vehicle"

    # [1]-1-2 PROTECTED ATTRIBUTE
    _fuel_capacity = 50   # Convention: should not be accessed directly

    # [1]-1-3 PRIVATE ATTRIBUTE
    __engine_number = "ENG-12345"  # Completely hidden outside the class


    # [1]-2 PUBLIC METHOD
    def show_info(self):
        print("Brand:", self.brand)
        print("Fuel capacity:", self._fuel_capacity)
        print("Engine number:", self.__engine_number)


    # [2]-1 NEW PUBLIC METHOD (safe access demo)
    def show_attributes(self):
        print("Fuel capacity:", self._fuel_capacity)
        print("Engine number:", self.__engine_number)

    # [3]-1 GETTER METHOD
    def get_engine_number(self):
        return self.__engine_number


    # [3]-2 SETTER METHOD
    def set_engine_number(self, new_number):
        # (optional simple validation for demo; keep it very basic)
        if isinstance(new_number, str) and new_number.strip():
            self.__engine_number = new_number
        else:
            print("Invalid engine number. Update skipped.")



# [1]-3 CREATE OBJECT
car = Vehicle()


# [1]-4 CALL METHOD
# car.show_info()

# [1]-5 TRY TO ACCESS ATTRIBUTES DIRECTLY
# print("Public brand:", car.brand)
# print("Protected fuel capacity (not recommended):", car._fuel_capacity)

# Uncommenting the next line would cause an error
# print("Private engine number:", car.__engine_number)


# [2]-2 ACCESS PROTECTED ATTRIBUTE (works, but not recommended)
# print("Accessing protected fuel capacity:", car._fuel_capacity)

# [2]-3 TRY TO ACCESS PRIVATE ATTRIBUTE (this would raise an error)
# Uncommenting the next line would cause an error:
# print("Accessing private engine number:", car.__engine_number)

# [2]-4 USE METHOD TO ACCESS PRIVATE ATTRIBUTE SAFELY
# car.show_attributes()

# [3]-3 USE GETTER
print("Engine number (via getter):", car.get_engine_number())

# [3]-4 USE SETTER
car.set_engine_number("ENG-98765")

# [3]-5 USE GETTER AGAIN
print("Updated engine number (via getter):", car.get_engine_number())
