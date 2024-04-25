#!/usr/bin/python3

# O(n**2)

def bubbleSort(alist):
    sizeList = len(alist)
    while (sizeList - 1) >= 0:
        for i in range(sizeList - 1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        sizeList = sizeList - 1
        print(alist)
        
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


alist = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
bubbleSort(alist)
print(alist)