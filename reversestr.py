#!/usr/bin/python3

import functools

letters = "ABCDEF"

print(letters)


print (letters[::-1])

ll = list(letters)

print (ll)

ll.reverse()

print (ll)

for i in range(len(ll)):
    print (ll[i], end = "")

print()


def reversed_string(text):
    return functools.reduce(lambda a, b: b + a, text)

print (reversed_string("Hello, World!"))


# Queue

mysrt = "Sogra"

print(mysrt)

myls = list(mysrt)

print(myls)

for i in range(len(mysrt)):
    print(myls.pop(), end = "")
print()


