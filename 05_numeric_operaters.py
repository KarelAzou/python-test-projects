import math
import random
import datetime
# --------------------
# Operations on strings
# --------------------


# ----------------------------------------------------------------
# Built_in functions
# - type
# - int()       | convert to int
# - float()     | convert to float
# - complex()   | convert to complex
# - abs()
# - round()

print(round(3.1856453, 2))
print(round(3.5))

# ----------------------------------------------------------------
# Operators
#  +        | add
#  -        | subtract
#  *        | multiply
#  /        | divide
#  //       | floor divide
#  %        | Modulo (returns remainder of the division)
#  **       | exponentiation (power)

print(9/2)
print(9//2)
print(9 % 2)
print(10**4)

x = 2
x += 3  # same as x + 3   = 5
x -= 1  # = 4
x *= 2  # = 8
print(x)

# ----------------------------------------------------------------
# from Math module
# ----------------------------------------------------------------
print("math.ceil(9.1):", math.ceil(9.145))  # Round up
print("math.floor(9.9):", math.floor(9.9154))  #
print(int(9.9))
print(math.trunc(9.546453))  #usign truc makes it more obvious what we're doing  as apposed to using int

z = 2 + 3j
print(z)

# ----------------------------------------------------------------
# numpy
import numpy as np
# print(np.__version__)

num = 9.3226
rounded_up = np.floor(num * 100) / 100


# ----------------------------------------------------------------
# advanced math

print(math.sqrt(12))
print(math.sin(180))
print(math.cos(360))
print(math.log(10000,10))
# look into it, there is alot!
# https://docs.python.org/3/library/math.html

# ----------------------------------------------------------------
# random

print(random.random()) #random between 0 and 1  
print(random.randint(1,6)) #random between 1 and 6


# ----------------------------------------------------------------
# verify numbers
x= 7.0
print(f"{x} as an integer?: {x.is_integer()}")
x= 7.1
print(f"{x} as an integer?: {x.is_integer()}")

#verify if my data is indeed op a specific datatype
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, str))
print(isinstance(x, datetime.date))
print(isinstance(x, datetime.datetime))
print(isinstance(x, datetime.time))


#I generate 100 random dice rolls and I want to count how often each number occured
numbers = []
for i in range (100):
    numbers.append(random.randint(1,6))

# or better: numbers = [random.randint(1, 6) for _ in range(100)]

print(numbers)
print("whut?")
# options 1 use collections.counter
from collections import Counter
counts = Counter(numbers)
counts = sorted(counts.items(), reverse=True)   #reverse sort 

print(f"sorted counts: {counts}")

# option 2, manually
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

counts = sorted(counts.items())

print(f"counts: {counts}")

# option 4 Using pandas (Overkill unless you're already using it)
# import pandas as pd 
# numbers = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, ...]
# series = pd.Series(numbers)
# counts = series.value_counts().sort_index()


# ----------------------------------------------------------------
#using map and lambda 
# A lambda function is a small anonymous function.
a = [1, 2, 3, 4, 5]

res = map(lambda num: str(num) + 
          (" Even" if num % 2 == 0 else " Odd"), a)

print("\n".join(res))

# ----------------------------------------------------------------
# a map function will apply a function for all values in the second argument (of type iterable)
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))
#result is a list of integers [1,2,3,4]


