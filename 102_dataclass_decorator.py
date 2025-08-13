# ------------------------------------------------
# using te dataclass decorator we don't need to impliment the ini and str dunder methods and those are not the only benefits.
from dataclasses import dataclass


@dataclass
class person:
    name: str
    age: int
    friends: list[str]


bob = person("bob", 29, ["Linda", "Teddy"])

print(bob)


# ------------------------------------------------
# alternative in a normal class, takes a lot more coding


class person2:
    def __init__(self, name: str, age: int, friends: list[str]) -> None:
        self.name = name
        self.age = age
        self.friends = friends

    def __str__(self) -> str:
        return f"person(name='{self.name}', age={self.age}, friends={self.friends})"


bob = person2("bob", 29, ["Linda", "Teddy"])

print(bob)

# ------------------------------------------------
# now lets add order = True to the decorator. makes it sortable ( by first property by default)
@dataclass(order=True)
class person3:
    name: str
    age: int
    friends: list[str]

bob = person3("Bob", 29, ["Linda", "Teddy"])
linda = person3("Linda", 28, ["Bob", "Teddy"])
mort = person3("Mort", 40, [])
bob2 = person3("Bob", 29, ["Linda", "Teddy"])

print(bob == bob2)
print(bob is bob2)

print(bob > bob2)
print(bob > linda)

print(sorted([bob,bob2,linda,mort]))
print(sorted([bob,bob2,linda,mort], key = lambda person : person.age, reverse = True))
print(bob)

# ------------------------------------------------
# lets make our dataclass immutable
@dataclass(frozen=True)
class person3:
    name: str
    age: int
    friends: list[str]

bob = person3("Bob", 29, ["Linda", "Teddy"])

try:
    bob.name = 'Louise' # won't work
except Exception as e :
    print(repr(e))

# ------------------------------------------------
# lets add computed properties to our dataclass
@dataclass
class Rectangle:
        width: float
        height: float

        @property
        def area(self) -> float:
            return self.width * self.height
        
        @property
        def perimiter(self) -> float:
            return 2*(self.width + self.height)
        
        def describe(self) -> None:
            print(f"{self}")
            print(f"Area:{self.area}")
            print(f"Perimeter: {self.perimiter}")

cube = Rectangle(2,2)

print(f"cube: {cube}")
cube.describe()
print(f"perim: {cube.perimiter}")