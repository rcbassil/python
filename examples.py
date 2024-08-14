#!/usr/bin/python3

from collections import deque, namedtuple
import csv
from functools import reduce
import math


print(2+3)
print(2>3)

print([3,True,"abacate",5])

mylist=[3,True,"abacate",5]

print(len(mylist))

print(mylist[1:3])

for item in mylist:
    print(item)


myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)


mylist=[3,1,4,6]

mylist.append(7)
print(mylist)
mylist.insert(2,5)
print(mylist)
print(mylist.pop())
print(mylist)
print(mylist.pop(1))
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
print(mylist.count(5))
print(mylist.index(4))
mylist.remove(5)
print(mylist)
del mylist[0]
print(mylist)

print(mylist+[8,9])

print(list(range(10)))
print(list(range(10,1,-1)))
print(list(range(5,10,2)))

myName="Rodrigo"
print(myName[1:3])
myNameList=list(myName)
myNameList.reverse()
print(myNameList)

for i in myNameList:
    print(i, end='')

print()

print(myName.upper())
print(myName.split('i'))

myTuple = (2,True,4.96)

print(myTuple)
print(len(myTuple))
print(myTuple + (3,8))

mySet={1,4,5,9}
print(mySet)

print(8 in mySet)

print(1 in mySet)

mySet.add("house")
print(mySet)

mySet.remove(4)
print(mySet)

print(mySet.pop())
print(mySet)

mySet.add(5)
print(mySet)

mySet.clear()
print(mySet)


capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals)
print(capitals['Iowa'])

capitals['Utah']='SaltLakeCity'
print(capitals)

print(len(capitals))

for k in capitals:
   print(capitals[k]," is the capital of ", k)

for k,v in capitals.items():
    print(k,v)

print(list(capitals))
print(list(capitals.items()))

print(list(capitals.keys()))
print(list(capitals.values()))

counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

for item in range(5):
   print(item**2)

n=5

if n<0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))

score=82

if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')


sqlist=[x*x for x in range(1,11)]
print(sqlist)

sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)

def square(n):
   return n**2

def double(n):
    return n*2

print(square(3))

def variableParams(*params):
   for i in params:
      print("Achei ", i)

variableParams(3,5,1,0)


sum = lambda x, y : x + y

print(sum(3,4))


# If one list has fewer elements than the others, 
# map will stop when the shortest list has been consumed

squareLambda = lambda x,y : (x**2, y**2)

l1 = [3,5,7,8]
l2 = [1,9,2]

SQ = map(squareLambda, l1, l2)
print(list(SQ))


l1 = [3,5,7,8]
l2 = [1,9,2,4]

SQ = map(squareLambda, l1, l2)
print(list(SQ))


def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res
family_of_functions = (math.sin, math.cos, math.tan)
print(map_functions(math.pi, family_of_functions))


def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(list(map(func, x)))
     return res
family_of_functions = (square, double)
print(map_functions([2,3,4,5], family_of_functions))


fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2 == 1 , fibonacci))
print(odd_numbers)

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
even_numbers = list(filter(lambda x: x % 2 == 0 , fibonacci))
print(even_numbers)


# maximum of a list of numerical values by using reduce

f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

f = lambda x, y: x+y
print(reduce(f, range(1,101)))


# Read csv files into dictionary

result = {}
count = 1

f=open("example.txt","r")
first_line = f.readline()
for i in first_line.strip().split(';'):
    result[str(count)+ " " +i] = []
    count = count+1
#print(result)
lines=f.readlines()
cnt = 0

for k in result.keys():
    if str(cnt+1) in k:
        for x in lines:
            v = list(result[k])
            #print(v)
            v.append(x.strip().split(';')[cnt])
            result[k]= v
            #print(list(result[k]))
    cnt = cnt+1
    
f.close()


print(result)



# read csv file to a list of dictionaries
with open('example.txt', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    data = [row for row in csv_reader]
print(data)


# Stacks

myStack = []

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)
myStack.pop()
print(myStack)


myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')
print(list(myStack))
myStack.pop()
print(list(myStack))


def convertToBinary(decNumber):
    remstack = deque()

    while decNumber > 0:
        rem = decNumber % 2
        decNumber = decNumber // 2
        remstack.append(rem)

    binString = ""
    while len(remstack):
        binString = binString + str(remstack.pop())

    return binString

print(convertToBinary(6))


# Queues

customers = deque()

# People arriving
customers.append("Jane")
customers.append("John")
customers.append("Linda")

print(list(customers))

# People getting tables
customers.popleft()
print(list(customers))


# Deque palindrome

myPalindrome = deque()
myPalindrome.append('r')
myPalindrome.append('a')
myPalindrome.append('d')
myPalindrome.append('a')
myPalindrome.append('r')

isPalindrome = True

while len(myPalindrome) > 1 and isPalindrome:
    last = myPalindrome.pop()
    first = myPalindrome.popleft()
    if last != first:
        isPalindrome=False

print(isPalindrome)

# Another way to check

myPalindrome = deque()
myPalindrome.append('r')
myPalindrome.append('a')
myPalindrome.append('d')
myPalindrome.append('a')
myPalindrome.append('r')

print(myPalindrome)
myPalindrome.reverse()
print(myPalindrome)


# Named Tuple

def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))

result = custom_divmod(12, 5)
print(result)


Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
print(point)
print(point.x)
print(point.y)


