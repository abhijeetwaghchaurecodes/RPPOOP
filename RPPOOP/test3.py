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

while True:
    print("Please select an option:")
    print("1. Calculate area of triangle")
    print("2. Calculate area of rectangle")
    print("3. Calculate area of square")
    print("4. Calculate area of hexagon")
    print("5. Calculate area of pentagon")
    print("6. Calculate area of heptagon")
    print("0. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            a = float(input("Enter length of side a: "))
            b = float(input("Enter length of side b: "))
            c = float(input("Enter length of side c: "))
            if a + b > c and b + c > a and c + a > b:  # Check for valid triangle
                t = Triangle(a, b, c)
                print("Area of triangle is:", t.get_area())
            else:
                print("Invalid input. Sides do not form a valid triangle.")
        
        elif choice == 2:
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            r = Rectangle(length, width)
            print("Area of rectangle is:", r.get_area())
        
        elif choice == 3:
            side = float(input("Enter length of square: "))
            s = Square(side)
            print("Area of square is:", s.get_area())

        elif choice == 4:
            side = float(input("Enter length of hexagon: "))
            h = Hexagon(side)
            print("Area of hexagon is:", h.get_area())
        
        elif choice == 5:
            side = float(input("Enter length of pentagon: "))
            p = Pentagon(side)
            print("Area of pentagon is:", p.get_area())
        
        elif choice == 6:
            side = float(input("Enter length of heptagon: "))
            h = Heptagon(side)
            print("Area of heptagon is:", h.get_area())
        
        elif choice == 0:
            break
    
        else:
            print("Invalid input. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid option (numeric value).")

    
