#!/usr/bin/python3

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        #print(midpoint)
        #print(alist[midpoint])
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint],item)
            else:
                return binarySearchRecursive(alist[midpoint+1:],item)
	

testlist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(binarySearchRecursive(testlist, 8))
print(binarySearchRecursive(testlist, 16))
