# --------------------
# Learning about the input function
# --------------------
# examples = int , bool, str, float
# list, set ,tuple , dict
# --------------------

# basics
# import re
# import unicodedata
from datetime import datetime, date

a = 10  # int
b = 3.15  # float
c = "Hello"  # str
d = 'Hi'  # str
e = '1234'  # str
f = True  # Bool
g = False  # Bool
h = None  # null,nothing
i = ""  # Str BLANK (Empty string)
j = " "  # str Empty space


# --------------------
# Full List of Datatypes
# --------------------

None  # No Value

int  # Numeric, int: 15
float  # Numeric, float: 3.15
complex  # Numeric, complex: 3 + 5j

str  # string 'hello'

bool  # boolean True/False


# date and time types
mydate = date.today()  # Date & Time , date: 2025-08-07
print(date)
mydate = datetime.now().date()  # Date & Time , date: 2025-08-07
print(date)
time = datetime.now().time()  # Date & Time , time: 12:29:00
print(time)
mytime = time.strftime('%H:%M:%S')
print("mytime", mytime)
print("type", type(mytime))

# Date & Time , date:   2025-08-07 12:29:00
mydatetime = datetime.now()
print(mydatetime)

customtime = date(2025, 12, 31)
print(customtime)
print("type", type(customtime))

# Multi- Values

mylist = [1, 2, 3, 4, 5]  # List
print("mylist", mylist)
myset = {1, 2, 3, 4, 5}  # Set
print("myset", myset)
mytuple = (1, 2, 3, 4, 5)  # Tuple
print("mytuple", mytuple)
mydict = {"a": 1, "b": 2, "c": 3}  # Dict
print("mydict", mydict)
myArray = ['i', [10, 20]]  # Array (List in Python)
print("myArray", myArray)

# --------------------
# we can define variables as having a certain datatype. 
# This will cause warnings in our sourcecode when developing but on't throw errors in runtime if we don't respect these types:

# For example of type hint on a variable. 
Age: int = 10 

# the same can be done on functions, both for input variables as outputs. for no output, we can even define output None
def print_age(age: int) -> None:
    print(f"The given age is {age}")


# the same can be done on functions, both for input variables as outputs. for no output, we can even define output None
def validate_email(email_input: str) -> bool:
    if email_input == 'bb':
        return False
    return True

print(validate_email(11))   # as expected the type checker indicates 11 is not a string

# --------------------
# Constants 

# Again python won't enforce this at runtime, but our type checker should warn is not to alter a constant , if we use Final
# we do need to set or type checker, pylance to strict "python.analysis.typeCheckingMode" = "standard" or higher in our settings.json
from typing import Final

VERSION: Final[str] = '10.0.0.1'
VERSION = '10.2'
print(VERSION)



# more examples of defining datatypes to be used on fuctions
def validate_email(email_input: str) -> bool:
    if email_input == 'bb':
            return False 
    return True

validate_email("bob@burgers.com")
print(validate_email("valid"))

class Car:
    def __init__(self, make: str , maxspeed: int) -> None:
        self.make: str = make
        self.maxspeed: int = maxspeed
    
    def __str__(self) -> str:
        return self.make

    def chiptune(self, speed_increase: int) -> None:
        self.maxspeed += speed_increase


toyota  = Car("Toyota", 150)
print(toyota)
toyota.chiptune(30)
print(toyota.maxspeed)
