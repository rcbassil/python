#!/usr/bin/python3

from collections import Counter


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict1['Name'])
print ("dict['Age']: ", dict1['Age'])

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2['Age'] = 8; # update existing entry
dict2['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict2['Age'])
print ("dict['School']: ", dict2['School'])

dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict3['Name'] # remove entry with key 'Name'

print(dict3)

# keys must be immutable such as strings, numbers and tuples.

dict4 = {('Name'): ('Zara','Aba'), 'Age': 7}
print ("dict4['Name']: ", dict4['Name'])

dict5 = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict5.get('Age'))
print ("Value : %s" %  dict5.get('Sex', "NA"))

print(dict5['Age'])


dict6 = {'Name': 'Zara', 'Age': 7}

print ("Age" in dict6)

print ("Sex" in dict6)

print (dict6.keys())
print (dict6.values())
print (dict6.items())

myl = []

for k,v in dict6.items():
    if v == 7:
        print("Age")
        myl.append(k)

print(myl)
        

# *************
# duplicates and unique

a = [1,2,3,2,1,5,6,5,5,5]

seen = set()
for x in a:
    if x not in seen:
        seen.add(x)

print(seen)

seen = set()
dupes = []

for x in a:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)

print(seen)
print(list(set(dupes)))


# Count how many times each item appears

mydict = {}

for i in a:
    #print(i)
    if i in mydict.keys():
        mydict[i] =  mydict[i] + 1
    else:
        mydict[i] = 1

print(mydict)

if 2 in mydict:
    print("Test")

# Duplicates and Uniques

mydup = []
myuniq = []

for k,v in mydict.items():
    if v >= 2:
        mydup.append(k)
    elif v == 1:
        myuniq.append(k)



print(mydup)
print(myuniq)


# Using Counter

myc = Counter(a)
print(myc)
most_common = myc.most_common()
print(most_common)
most_common.reverse()
print(most_common)

testlist = [1,3,4,5,1,2,6,8]

print(testlist[-8:3])

print(set(testlist))
