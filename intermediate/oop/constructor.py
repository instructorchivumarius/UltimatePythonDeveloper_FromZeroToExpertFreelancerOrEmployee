# Other Special Methods
# We continue with the Person class and add more special methods.

# (1) DEFINE CLASS PERSON WITH SPECIAL METHODS
class Person:
    # (1-1) CONSTRUCTOR
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # (1-2) __str__ METHOD
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # (1-3) __len__ METHOD
    def __len__(self):
        return self.age

    # (1-4) __del__ METHOD
    def __del__(self):
        print(f"Object {self.name} is being deleted.")

# (2) CREATE OBJECT
p1 = Person("Alice", 25)

# (3) USE __str__ METHOD
print(p1)

# (4) USE __len__ METHOD
print("Age (via len):", len(p1))

# (5) DELETE OBJECT
del p1
