#!/usr/bin/python3

from collections import Counter

print ("Hello, Python!")

myl = [1,3,4,5]

print (len(myl))

mystr = "My text to be reversed"

print(mystr)

print(list(mystr.split()))

mynl = list(mystr.split())

mynl.reverse()

print(mynl)

for i in mynl:
    print (i, end = ' ')
print()

mystr = "Minha string pra ser revertida"

print(list(reversed(mystr.split())))

########

t1 = Counter('aaabbbbchhaaaaaappppyyyiiirrrttpdaoph')

print(t1)

del(t1["b"])

myl = ['h','a','p','y']

t2 = Counter()

for k,v in t1.items():
    if k in myl:
        t2[k] = v

print(t2)

t3 = Counter('happy')

print(t3)


count = 0
naozero = True

while naozero:
    t4 = t2 - t3
    if len(t2.keys()) < len(t3.keys()): 
        naozero = False
    else:
        t2 = t4
        count = count+1
        print(t4)

print(count)