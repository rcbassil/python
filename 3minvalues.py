#!/usr/bin/python3

from functools import reduce

l = [47,11,42,102,13]

l.sort()

print(l[:3])

for i in range(0,3):
    print (l[i])

l = [47,11,42,102,13]

for i in range(0,3):
    f = lambda a,b: a if (a < b) else b
    minv = reduce(f, l)
    print (minv)
    l.remove(minv)



