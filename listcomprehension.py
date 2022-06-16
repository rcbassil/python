#!/usr/bin/python3

from math import sqrt


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)



print([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])


colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)


noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)


# Set comprehension

n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)}
no_primes

primes = {i for i in range(2, n) if i not in no_primes}
print(primes)


# Generator comprehension

x = (x **2 for x in range(20))
print(x)
x = list(x)
print(x)


# Primes

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p

    
for i in range(1,50):
    print(i, primes(i))