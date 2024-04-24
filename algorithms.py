#!/usr/bin/python3

import string
import random
import sys
from Fraction import Fraction
from Queue import Queue
from Stack import Stack

myvar = 0

print(myvar)

myvar = "Test"

print(myvar)

myvar = [1,3,5,6]

print(len(myvar))

print(myvar)

print(1 in myvar)

print(myvar.pop())

print(myvar)

print(list(range(10)))

mystring = "Rodrigo"

print(mystring.find("o"))
print(mystring)
print(mystring*2)
print("r" in mystring)
print("s" in mystring)
print(len(mystring))
print(mystring[-3])
print(mystring + " Bassil")

mytuple = ()
print(mytuple)

mytuple = (5,)
print(mytuple + (3,))
print(mytuple[0])

print(set(mystring))
print("i" in set(mystring))

myset = set(mystring)
myset.add("s")
myset.remove("i")
print(myset)


capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}

print(capitals)
print(len(capitals))
print("Iowa" in capitals)
print("Iowa" in capitals.keys())
print("DesMoines" in capitals.values())
print(capitals.items())
print(capitals.get("Iowa"))
print(capitals["Iowa"])
print(list(capitals.items()))
print(list(capitals.values()))

capitals["Quebec"] = "Montreal"
print(capitals)


for item in range(5):
    print(item**2)


for i in mystring:
    print(i)

for i in capitals:
    print(i)

for i,j in capitals.items():
    print(i,j)


wordlist = ['cat','dog','rabbit']

letterlist = set()
for aword in wordlist:
    for aletter in aword:
        letterlist.add(aletter)
print(letterlist)


sqlist=[]
for x in range(1,11):
    sqlist.append(x*x)

print(sqlist)

sqlist=[x*x for x in range(1,11)]
print(sqlist)

sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)

sqlist=[x*x for x in range(1,11) if x%2 == 0]
print(sqlist)

def square(n):
    return n**2

print(square(square(3)))


#Infinite Monkey Theorem start

def generate(length):
    characters = string.ascii_lowercase+" "
    return "".join([random.choice(characters) for i in range(length)])

phrase = "methinks it is like a weasel"

print(generate(len(phrase)))

generatedString = generate(len(phrase))

def score(test_string,target_string):
    test_list = zip([i for i in test_string],[i for i in target_string])
    return (sum([1 for test_letter, target_letter in test_list if test_letter == target_letter])/len(target_string))*100

print(score(generatedString, phrase))

#Infinite Monkey Theorem end

myfraction = Fraction(3,5)
print(myfraction)

myfraction.show()

f1 = Fraction(3,5)
f2 = Fraction(4,2)

print(f1+f2)

wordlist = ['cat','dog','rabbit']

print(wordlist)
del wordlist[0]
print(wordlist)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()

print(q)


myl = [4,6,2,3,9]

print(myl)

myl.reverse()

print(myl)


mystack = Stack()


mystack.push(4)
mystack.push(6)
mystack.push(2)
mystack.push(3)
mystack.push(9)

print(mystack)

myl = []

myl.append(mystack.pop())
myl.append(mystack.pop())
myl.append(mystack.pop())
myl.append(mystack.pop())
myl.append(mystack.pop())

print(myl)


