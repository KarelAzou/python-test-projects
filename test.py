#----------------------
# Decorators
# Let us modify functions without changing their code
# https://www.geeksforgeeks.org/python/decorators-in-python/
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