#!/usr/bin/python3

import string
import random
import sys
from Fraction import Fraction
from Queue import Queue
from Stack import Stack
from UnorderedList import UnorderedList
from HashMap import HashTable
from BinaryHeap import BinHeap
from BinarySearchTree import BinarySearchTree
from Graph import Graph
from Vertex import Vertex

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


myUnorderedList = UnorderedList()
print(myUnorderedList.isEmpty())

myUnorderedList.add(2)
myUnorderedList.add(8)
myUnorderedList.add(12)
myUnorderedList.add(3)
print(myUnorderedList.isEmpty())
print(myUnorderedList)
print(myUnorderedList.size())
print(myUnorderedList.search(8))
print(myUnorderedList.search(18))
print(myUnorderedList)
print(myUnorderedList.remove(2))
print(myUnorderedList.remove(8))
print(myUnorderedList.remove(12))
print(myUnorderedList.remove(3))
print(myUnorderedList.isEmpty())
print(myUnorderedList.remove(3))


def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    

print(factorial(4))


strStack = Stack()

def toStr(n,base):
   response = ""
   convertString = "0123456789ABCDEF"
   while n > 0:
       strStack.push(convertString[n%base])
       n = n//base

   while not strStack.isEmpty():
       response = response + str(strStack.pop())

   return response
       

print(toStr(10,16))

mylist = [1, 4, 5, 6 ,7, 2]

def findElement(element,listOfElements):
    found = False
    for i in listOfElements:
        if i == element:
            found = True
            break

    return found


print(findElement(6,mylist))
print(findElement(2,mylist))
print(findElement(8,mylist))
print(findElement(1,mylist))


H=HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print(H.slots)
print(H.data)


H[20]='duck'
print(H.data)
print(H[26])



# trees

my_tree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(my_tree)
print('left subtree = ', my_tree[1])
print('root = ', my_tree[0])
print('right subtree = ', my_tree[2])


# binary heap

myBinaryHeap = BinHeap()
myBinaryHeap.buildHeap([5,3,9,8,12,14,4])
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())
print(myBinaryHeap.delMin())

# binary search tree

myBinSearchTree = BinarySearchTree()
print(myBinSearchTree)

myBinSearchTree[3]="red"
myBinSearchTree[4]="blue"
myBinSearchTree[6]="yellow"
myBinSearchTree[2]="at"

print(myBinSearchTree[6])
print(myBinSearchTree[2])

# graph

g = Graph()

for i in range(6):
    g.add_vertex(Vertex(i))

print(g.vertices)

for v in g:
    print(v)

g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 9)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 8)
g.add_edge(5, 2, 1)

for v in g:
    print(v)


print(g.get_vertices())
print(g.get_vertex(0))

for v in g:
    print(v)
    for w in v.getConnections():
        print("({} -> {}, weight {})".format(v.key, w.key, v.getWeight(w)))

