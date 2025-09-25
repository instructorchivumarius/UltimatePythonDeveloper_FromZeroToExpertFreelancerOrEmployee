# Using super()
# We continue working in inheritance.py from the previous lessons.
# In this lesson we use super() to call the parent method.

# (1) DEFINE PARENT CLASS
class Animal:
    # (1-1) METHOD IN PARENT CLASS
    def speak(self):
        print("This animal makes a sound.")

# (2) DEFINE CHILD CLASS DOG
class Dog(Animal):
    # (2-1) OVERRIDE METHOD AND USE super()
    def speak(self):
        super().speak()   # call parent method
        print("The dog barks: Woof!")

# (3) DEFINE CHILD CLASS CAT
class Cat(Animal):
    # (3-1) OVERRIDE METHOD AND USE super()
    def speak(self):
        super().speak()   # call parent method
        print("The cat meows: Meow!")

# (4) CREATE OBJECTS AND USE METHODS
dog = Dog()
dog.speak()

cat = Cat()
cat.speak()
