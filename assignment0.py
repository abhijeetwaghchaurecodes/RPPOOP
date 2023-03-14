#ASSIGNMENT 0 - FINDING THE AREA AND PERIMETER OF DIFFERENT POLYGONS

#here first we need to import the 'math' library of python to include some basic constants like pi, tau, e, etc
#there's also a 'sum()' function in python, which gives the sum of the iterables 

#The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

#---- ENTIRE CODE ----

import math

class Shape():
    def __init__(self, num_sides, side_lengths):
        self.num_sides = num_sides
        self.side_lengths = side_lengths
        
    def get_perimeter(self):
        return sum(self.side_lengths)
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(3, [a, b, c])
        self.a = a
        self.b = b
        self.c = c
        
    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(4, [length, width, length, width])
        self.length = length
        self.width = width
        
    def get_area(self):
        return self.width * self.length
    
class Square(Rectangle):
    def __init__(self, sides):
        super().__init__(sides, sides)
        
class Hexagon(Shape):
    def __init__(self, side):
        super().__init__(6, [side, side, side, side, side, side])
        self.side = side
        
    def get_area(self):
        return round(2.598 * self.side * self.side, 3)

class Pentagon(Shape):
    def __init__(self, side):
        super().__init__(5, [side, side, side, side, side])
        self.side = side
        
    def get_area(self):
        return round(1.72 * self.side * self.side, 3)
    
class Heptagon(Shape):
    def __init__(self, sides):
        super().__init__(7, [sides,sides,sides,sides,sides,sides,sides])
        self.sides = sides
    def get_area(self):
        return round(3.633911 * self.sides * self.sides, 3)
    
        
#fetching the output
t = Triangle(3,4,5)
print("Area of the Triangle is: " ,t.get_area(), "sq.uints")
print("Perimeter of the Triangle: ", t.get_perimeter(), "units\n")

e = EquilateralTriangle(5)
print("Area of the Equilateral Triangle is: ",e.get_area(), "sq.units")
print("Perimeter of the Equilateral Triangle is: ", e.get_perimeter(), "units\n")
r = Rectangle(4.3,2.7)
print("Area of the Rectangle: ", r.get_area(), "sq.uints")
print("Perimeter of the Rectangle: ", r.get_perimeter(), "units\n")

s = Square(4)
print("Area of the Square is: ", s.get_area(), "sq.uints")
print("Perimeter of Square is: ", s.get_perimeter(), "units\n")

h = Hexagon(7)
print("Area of the Hexagon is: ", h.get_area(), "sq.uints")
print("Perimeter of Hexagon is: ", h.get_perimeter(), "units\n")

p = Pentagon(5)
print("Area of the Pentagon is: ", p.get_area(), "sq.uints")
print("Perimeter of Pentagon is: ", p.get_perimeter(), "units\n")

hept = Heptagon(5)
print("Area of the Heptagon is: ", hept.get_area(), "sq.units")
print("Perimeter of Heptagon is: ", hept.get_perimeter(), "units\n")
