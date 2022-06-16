#!/usr/bin/python3

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


