#!/usr/bin/python3

def test1():
    l = []
    for i in range(1000):
        l = l + [i]
    print(l)

def test2():
    l = []
    for i in range(1000):
        l.append(i)
    print(l)

def test3():
    l = [i for i in range(1000)]
    print(l)

def test4():
    l = list(range(1000))
    print(l)


test1()
test2()
test3()
test4()