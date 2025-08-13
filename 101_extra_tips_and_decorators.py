
#https://www.youtube.com/watch?v=mB0EBW-vDSQ

#----------------------
# use context managers 
# No need to remember to close the file
with open('data.txt', 'r') as file:
    content = file.read()
# the file is automatically closed here, even if exceptions occur


#----------------------
# Dictionary and Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
commin = set_a & set_b # {3,4 }

# Dictionary comprehentions
user_scores = {name: score for name, score in zip(users, scores)}


#----------------------
# Decorators
# Let us modify functions without changing their code
# https://www.geeksforgeeks.org/python/decorators-in-python/
# A simple decorator function
from datetime import datetime
def mydecorator(func):
  
    def wrapper():
        print(f"Before calling the function {datetime.now()}.")
        func()
        print(f"After calling the function datetime.now()}.")
    return wrapper

# Applying the decorator to a function
@mydecorator
def greet():
    print("Hello, World!")

greet()

#----------------------
# A simple decorator function to measure tame taken of a function:
import time
def timer(func):
  
    def wrapper():
        t1 = time.time()
        res = func()
        t2 = time.time()
        print(f"function {str(func.__name__)} took {round((t2 - t1)* 1000,4)} ms")
    return wrapper

# Applying the decorator to a function
@timer
def greet():
    print("Hello, World!")

greet()

#----------------------
# @staticmethod
# The @staticmethod decorator is used to define a method that doesn't operate on an instance of the class (i.e., it doesn't use self). Static methods are called on the class itself, not on an instance of the class.
# add is a static method defined with the @staticmethod decorator.
# It can be called directly on the class MathOperations without creating an instance.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)


#----------------------
# @classmethod

# The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of the class.
# Example:

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
e_bob = Employee('Linda', 500)
e_linda = Employee('Bob', 400)

print(e_bob.raise_amount)
print(e_bob.raise_amount)
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

print(e_bob.raise_amount)
print(e_bob.raise_amount)

#----------------------
# @property
# The @property decorator is used to define a method as a property, which allows you to access it like an attribute. This is useful for encapsulating the implementation of a method while still providing a simple interface.
# radius and area are properties defined with the @property decorator.
# The radius property also has a setter method to allow modification with validation.
# These properties provide a way to access and modify private attributes while maintaining encapsulation.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)