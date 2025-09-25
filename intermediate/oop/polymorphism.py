# Polymorphism in Methods and Functions
# We continue from Lesson Polymorphism.
# Now we use polymorphism inside a function.

# (1) DEFINE PARENT CLASS SHAPE
class Shape:
    def draw(self):
        print("Drawing a generic shape.")

# (2) DEFINE CHILD CLASS CIRCLE
class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

# (3) DEFINE CHILD CLASS SQUARE
class Square(Shape):
    def draw(self):
        print("Drawing a square.")

# (4) DEFINE CHILD CLASS TRIANGLE
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle.")

# (5) FUNCTION THAT USES POLYMORPHISM
def show_shape(shape):
    shape.draw()  # same function works for any object with draw()

# (6) CREATE OBJECTS
c = Circle()
s = Square()
t = Triangle()

# (7) CALL FUNCTION WITH DIFFERENT OBJECTS
show_shape(c)
show_shape(s)
show_shape(t)
