# --------------------
# Learning about the input function
# --------------------
# examples = int , bool, str, float
# list, set ,tuple , dict
# --------------------

# basics
import re
import unicodedata
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