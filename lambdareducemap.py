#!/usr/bin/python3
import subprocess,functools



C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 

list(map(lambda x, y, z : x+y+z, a, b, c))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2 !=0 , fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)


print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))

#Determining the maximum of a list of numerical values by using reduce

f = lambda a,b: a if (a > b) else b
print(functools.reduce(f, [47,11,42,102,13]))

functools.reduce(lambda x, y: x+y, range(1,101))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print (less_than_zero)


def multiply(x):
  return (x*x)

def add(x):
  return (x+x)

funcs = [multiply, add]
for i in range(5):
  value = list(map(lambda x: x(i), funcs))
  print(value)


mount = subprocess.getoutput('mount -v')
print(mount)
lines = mount.splitlines()
print(lines)
points = list(map(lambda line: line.split()[2], lines))
print (points)
