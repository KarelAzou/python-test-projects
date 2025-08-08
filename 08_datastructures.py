# 🧠 Quick Examples of What to Use
# Situation	                                                    Use
# You need an ordered list of names	                            list
# You’re returning (x, y) coordinates from a function	        tuple
# You need to store config options or key-value data	        dict
# You want to remove duplicates from a list	                    set
# You want to check if a word appears in a large collection 	set
# You want to map usernames to scores	                        dict


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



# lists / Arrays
# https://www.w3schools.com/python/python_arrays.asp
# To use arrays , we must install and import Numpy

cars = ["Ford", "Volvo", "BMW"] 

# Get the value of the first array item:
x = cars[0] 
print(x)

# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

# Add one more element to the cars array:
cars.append("Honda") 
print(cars)
# Delete the second element of the cars array:
cars.pop(1)
print(cars) 

for x in cars:
    print(x) 

for x in range(3):
    print(cars[x]) 

# Delete the element that has the value "Volvo":
#The list's remove() method only removes the first occurrence of the specified value.
try:
    cars.remove("Volvo")  # ValueError: list.remove(x): x not in list 
except Exception as e :
    print(repr(e))

cars.remove("Honda") 
print(cars) 


list1 = ["abc", 34, True, 40, "male"]
print(type(mylist))



# Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Once a set is created, you cannot change its items, but you can add new items.

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Check if "banana" is present in the set:
print("banana" in thisset) 

# Add an item to a set, using the add() method:
thisset.add("orange")
print(thisset) 

# Add elements from tropical into thisset:
# note we can add any iterable to the set: Add Any Iterable
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #{'orange', 'cherry', 'apple', 'papaya', 'mango', 'banana', 'pineapple'}
print("Update with any iterable to add to the list:",thisset) 

# Adding the same item twice will not raise an error, but neither will it add to the set
thisset.add("orange")
print("Add orange:",thisset) 

# But it will work if the item is not exactly the same value ( case sensitive)
thisset.add("Orange")
print("Add Orange:",thisset) 

# Remove "banana" by using the remove() method:
# Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print("After remove banana:",thisset) 

# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print("After discard banana:",thisset) 

# Remove a random item by using the pop() method:
x = thisset.pop()   #x is the item you removed
print(x)
print(thisset) 

# The clear() method empties the set:
thisset.clear()
print(thisset) 

#The del keyword will delete the set completely:
del thisset
print(thisset)  # Raises a NameError:


# Join set1 and set2 into a new set: thsi also works with other iterables like lists or tuples, with dictionaries you'll only add the keys.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

# You can use the | operator instead of the union() method, and you will get the same result. THIS ONLY WORKS TO JOIN SETS
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) 

# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 

myset2 = set1 | set2 | set3 |set4
print(myset2) 

##
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) 

# set methods, interestign read: https://www.w3schools.com/python/python_sets_methods.asp