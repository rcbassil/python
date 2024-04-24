#!/usr/bin/python3

from collections import namedtuple

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

tup1 = (50,)


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples, updating or deleting(you can only delete the whole tuple, not elements) is not possible
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)


for x in (1,2,3) : print (x, end = ' ')

print()

print(tup2[1])

# named tuples

def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))


result = custom_divmod(12, 5)

print(result)
print(result.quotient)

Point = namedtuple("Point", ["x", "y"])

point = Point(2, 4)

print(point)
print(point.x)
print(point[0])

# Create a dictionary from a named tuple

print(point._asdict())

# Replace the value of a field

point = point._replace(x=34)

print(point)