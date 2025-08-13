# totday we'll learn abotu dunder, or dobuel inderscore.
# everything in python is an objec,t like a str, or an int, but even a function.

# __init__ # used to construct or define a new object, we define what we wantto happen when an object is created.

class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y


Rect(2, 3)


# ---------------------------------------------------------------------------
# example 1: + or __ADD__
str1 = "Hello"
str2 = "world"

new_str = str1 + str2  # + is mapping to a dunder function: __add__()

# alternative that does the same::
new_str = str1.__add__(str2)

# ---------------------------------------------------------------------------
# example 2: len or __len__

new_str = len(str1)
print(new_str)
# alt:
new_str = str1.__len__()
print(new_str)


# ---------------------------------------------------------------------------
# now lets make our own

class counter:
    def __init__(self):
        self.value = 1

    def count_up(self) -> int:
        self.value += 1

    def count_downm(self) -> int:
        self.value -= 1

    def __str__(self):    # method used whenver we print an object
        return f"Count={self.value}"
    
    def __add__(self, other) -> int:    # method used whenver use "+" on this class, whatever comes after the + is known as "other"
        if not isinstance(other, counter):
            raise TypeError("The second operator should be of type 'counter'")
        return self.value + other.value
    
count1 = counter()
count2 = counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2) # fail here as we don't have a "+" function



# ---------------------------------------------------------------------------
# more examples:
# __str__ : Meant for user friendly output
# __repr__ : representation output, mostly used for debugging is meant for more detailed, unambiguous output
# __add__ : + operator
# __sub__ : - operator  (for exampel add checks to make sure qty doesn't go below zero)
# __mul__ : * opratyor ()
# __true_div__ : / 
# __floor_div__ : //
# __eq__ : ==
# __ne__ : !=
# __lt__ : <
# __gt__ : >
# __let__ : <=
# __let__ : <=


# ---------------------------------------------------------------------------
# more examples:

lst = [1, 2, 3]
lst[1] # grab first of list.

# what is the slicing operator and dunder function?

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None    
        self.size = 0

    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        """Enable indexing (obj[index])."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def __setitem__(self, index, value):
        """Enable item assignment (obj[index] = value)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
    
    def __delitem__(self, index):
        """Delete an item (del obj[index])."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index -1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    ## def __contains__

    def __str__(self):
        """User_friendlt strign representation"""
        values=[]
        current = self.head
        while current:
                values.append(str(current.value))
                current = current.next
        return " -> ".join(values)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

## test this LinkedList

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll)
print(len(ll)) # output 3 
print(ll[1]) # output 20

ll[1] = 25
print(ll)
del ll[1]
print(ll)
print(30 in ll)

# ---------------------------------------------------------------------------
# context managers

class DatabaseConnection:
    def __init__(self, value):
        self.connected = False
        self.database_name = value

    def __enter__(self):
        """Establish the connection"""
        self.connected = True
        print(f"Connected to the database '{self.database_name}'.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """close the connection"""
        self.connected = False
        print(f"Disconnected from the database '{self.database_name}'.")
        # Handle any exceptions
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True # suppresses exceptions if they occur


with DatabaseConnection("ExampleDB") as db:    # using with runs the enter and exit dunder functions
        print(f"Is connected? {db.connected}")


# ---------------------------------------------------------------------------
# the "in" operator makes use of the __iter__ and __next__ dunder functions, they can be used operator to make our own iterator. For example to count down

class Counter:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self): 
        self.current = self.start
        return self

    def __next__(self): #while iterating this method is called time and time again untill StopIteration is thrown
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration
        
for num in Counter(5):
    print(num)
