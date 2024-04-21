#!/usr/bin/python3

list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print ("updated list : ", list1)


aList = [123, 'xyz', 'zara', 'abc', 123]

print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))


list1 = ['physics', 'chemistry', 'maths']
list2 = list(range(5))     #creates list of numbers between 0-4
print(list1+list2) # concatenation
list1.extend(list2)
print ('Extended List :', list1)



list1 = ['physics', 'chemistry', 'maths']
print ('Index of chemistry', list1.index('chemistry'))

list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print ('Final list : ', list1)

list1 = ['physics', 'Biology', 'chemistry', 'maths']
print(list1.pop())
print ("list now : ", list1)

list1.pop(1)
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.remove('Biology')
print ("list now : ", list1)
list1.remove('maths')
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)

for x in [1,2,3] : print (x, end = ' ')

print()

mys = "mystest"
myl = list(mys)

print (myl)

myl.reverse()

print(myl)


list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort", list1)
list1.sort()
print ("list after sort : ", list1)

print ("Ascending sort")

list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

print ("Descending sort")

list2.sort(reverse=True)

print ("list after sort : ", list2)



list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)

def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)


L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1 = L1+L2
print ("Joined list:", L1)

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print ("Joined list:", L1)

L1.pop(2)
print(L1)

lst = [10, 20, 45, 10, 30, 10, 55]
print ("lst:", lst)
c = lst.count(10)
print ("count of 10:", c)

lst = [25, 12, 10, -21, 10, 100]
print ("lst:", lst)
x = lst.index(10)
print ("First index of 10:", x)


L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for x in L1:
   if x not in L2:
      L2.append(x)
print (L2)

L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)