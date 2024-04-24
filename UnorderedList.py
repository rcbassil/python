#!/usr/bin/python3

from Node import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        removed = False
        current = self.head
        previous = None
        found = False
        while not found and current != None :
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None and current != None:
            self.head = current.getNext()
            removed = True
        elif previous != None and current != None:
            previous.setNext(current.getNext())
            removed = True

        return removed

    def __str__(self):
        mystr = ""
        current = self.head
        while current != None:
            mystr = mystr + " " + str(current.getData())
            current = current.getNext()
        
        return mystr
            