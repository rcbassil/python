#!/usr/bin/python3

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
	
    
    return found



#ordered list
ll = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(orderedSequentialSearch(ll,15))