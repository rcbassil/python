from collections import deque


myd = deque()

print(myd)

myd2 = deque("abcd")

print(myd2)

numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

myd3 = deque(numbers.items())

print(myd3)


numbers = deque([1, 2, 3, 4])
print(numbers)
print(numbers.popleft())
print(numbers)
numbers.appendleft(1)
print(numbers)
print(numbers.pop())
print(numbers)
numbers.append(4)
print(numbers)



letters = deque("abde")

print(letters)

letters.insert(2, "c")

print(letters)

letters.remove("d")

print(letters)

del letters[2]

print(letters)

print(letters[2])