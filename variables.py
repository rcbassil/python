#!/usr/bin/python3

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

a, b, c = 1, 2, "john"

print (a,b,c)

mystr = 'Hello World!'

print (mystr)          # Prints complete string
print (mystr[0])       # Prints first character of the string
print (mystr[2:5])     # Prints characters starting from 3rd to 5th
print (mystr[2:])      # Prints string starting from 3rd character
print (mystr * 2)      # Prints string two times
print (mystr + "TEST") # Prints concatenated string
print (mystr[-1])      # Prints last character

mylist = [ 'abcd', 786 , 2.23, 'john', 70.2, 786, 'abcd' ]
tinylist = [123, 'john']

mylist[2] = 2.25

print (mylist)          # Prints complete list
print (mylist[0])       # Prints first element of the list
print (mylist[1:3])     # Prints elements starting from 2nd till 3rd 
print (mylist[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (mylist + tinylist) # Prints concatenated lists
print (mylist[-1])      # Prints last element


mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

## Tuples can not be updated !!

print (mytuple)           # Prints complete tuple
print (mytuple[0])        # Prints first element of the tuple
print (mytuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (mytuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (mytuple + tinytuple) # Prints concatenated tuple
print (mytuple[-1])       # Prints last element


# Dictionaries have no concept of order among the elements.

mydict = {}
mydict['one'] = "This is one"
mydict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (mydict['one'])       # Prints value for 'one' key
print (mydict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


# Set in python is defined as the unordered collection of unique items having different data types inside a curly bracket {}
# set does not allow duplicate elements. If we use a set then the elements will be unique.

print (tuple(mylist))
print (set(mylist))

tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
mylist2 = [[11, "eleven"], [21, "mike"], [19, "dustin"], [46, "caleb"]]

print (dict(tup))
print (dict(mylist2))

# here, the first element of the tuple becomes a value, and the second element of a tuple becomes the key to the dictionary

dct = dict(map(reversed, tup))
print(dct)

# Convert a list of Tuples into Dictionary with value being a list

def conversion(tup, dict):
    for x, y in tup:
        dict.setdefault(x, []).append(y)
    return dict


tups = [("Boba", 21), ("Din", 19), ("Grogu", 46), ("Ahsoka", 11)]
tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
tup3 = ()

for x, y in tups:
   print (x)

for x, y in tups:
   print (y)

dictionary1 = {}
dictionary2 = {}

print(conversion(tups, dictionary1))

print(conversion(tup, dictionary2))

print(dict(tup))

print(tup3)


set2 = {1,1,1}
print(set2)
print(set(set2))



myvar = 100
if ( myvar  == 100 ) : print ("Value of expression is 100")
else:
    print("Not equal 100")


count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1


count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)


fruits = ['banana', 'apple',  'mango']

for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)



fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

myit = iter(fruits)

for x in myit:
   print(x)


numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')


for i in range(1,11):
   for j in range(1,11):
      k = i*j
      print (k, end=' ')
   print()


for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)

a = 10
b = 32
c = 12
d = 65

print(max(a,b,c,d))
print(min(a,b,c,d))


alist1 = [1,4,7,3]
alist2 = [1,4,8,3]

if alist1 == alist2:
   print("Equal")
elif alist1 != alist2:
   print("Not equal")
else:
   print("None")

if 1 in alist1:
   print("Found 1")

for i in range(10):
   print(i)

print(len("abcs"))