from collections import deque
from Queue2 import Queue


customers = deque()

customers.append("Jane")
customers.append("John")
customers.append("Linda")

print(customers)

customers.popleft()

print(customers)


numbers = Queue()

print(numbers)

for number in range(1, 5):
    numbers.enqueue(number)

print(numbers)

numbers.dequeue()

print(numbers)

print(numbers.__contains__(1))

print(numbers.__contains__(3))

print(list(numbers.__reversed__()))

four_numbers = deque([0, 1, 2, 3, 4], maxlen=4) # Discard 0

print(four_numbers)

print(four_numbers.maxlen)


# rotate

ordinals = deque(["first", "second", "third"])

print(ordinals)

# Rotate items to the right

ordinals.rotate()

print(ordinals)

ordinals.rotate(2)

print(ordinals)

# Rotate items to the left

ordinals.rotate(-2)

print(ordinals)

ordinals.rotate(-1)

print(ordinals)

numbers = deque([1,3,4,5,3,4])

print(numbers.index(3)) # returns index of 3

print(numbers.count(4)) # returns number of times the value 4 appears

numbers.reverse()

print(numbers)

print(sorted(numbers))

numbers.clear()

print(numbers)

numbers.extend([3, 4, 5])

print(numbers)

numbers.extendleft([-1, -2, -3, -4, -5])

print(numbers)


#########

myordinals = deque(["a", "b", "c","d","e","f","g"])
print(myordinals)

n = 0
while n < len(myordinals):
    myordinals.rotate()
    print(myordinals)
    n = n+1
    print(n)