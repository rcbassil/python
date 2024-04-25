#!/usr/bin/python3

# O(n**2)


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       

def myselectionSort(alist):
   sizeList = len(alist)
   while (sizeList - 1) >= 0:
       positionOfMax=0
       for i in range(sizeList):
           if alist[i]>alist[positionOfMax]:
               positionOfMax = i
               
       temp = alist[sizeList - 1]
       alist[sizeList - 1] = alist[positionOfMax]
       alist[positionOfMax] = temp
       sizeList = sizeList - 1



alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
myselectionSort(alist)
print(alist)