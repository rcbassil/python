#!/usr/bin/python3

from functools import reduce

l = [47,11,42,102,13]

l.sort()


print (l)

print(l[-1:])
print(l[-2:])

print (l[::-1]) # Same as reverse

print (l[:-4:-1])

print (l[:-2:-1])


l.reverse()

print(l)

print(l[1:5:2])

l = [47,11,42,102,13]

for i in range(0,3):
    f = lambda a,b: a if (a > b) else b
    maxv = reduce(f, l)
    print (maxv)
    l.remove(maxv)
