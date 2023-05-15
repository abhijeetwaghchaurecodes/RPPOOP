"""
Polymorphism is a concept in object-oriented programming that refers to the ability of an object or function to take on different forms or behaviors 
depending on the context in which it is used. In other words, it allows different objects to respond to the same message or method call in different ways.

There are two main types of polymorphism in OOP: runtime polymorphism and compile-time polymorphism.

[1] Runtime Polymorphism:
    Runtime polymorphism is also known as dynamic polymorphism. It occurs when a method or function is called at runtime, and the actual implementation of the method 
    or function is determined based on the object that is calling it.
    
[2] Compile-time Polymorphism:
    Compile-time polymorphism is also known as static polymorphism. It occurs when the type of an object or function is determined at compile-time rather 
    than runtime. This type of polymorphism is achieved through function overloading, which is a technique that allows a function to have multiple 
    implementations with different parameters.
"""

#RUN-TIME POLYMORPHISM
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

dog = Dog("Rufus")
cat = Cat("Whiskers")

make_sound(dog) # Output: Woof
make_sound(cat) # Output: Meow



#COMPILE-TIME POLYMORPHISM
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

calc = Calculator()

#print(calc.add(1, 2)) # Output: TypeError: add() missing 1 required positional argument: 'c'
print(calc.add(1, 2, 3)) # Output: 6