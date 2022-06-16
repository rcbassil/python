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
list1.pop()
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