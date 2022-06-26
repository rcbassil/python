from collections import deque


######### deque does not support slice or pop(index) !!!!!

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


########

ticket_queue = deque()

ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")

print(ticket_queue)

ticket_queue.popleft()

print(ticket_queue)

ticket_queue = deque()
ticket_queue.appendleft("Rod")
ticket_queue.appendleft("Cass")
ticket_queue.appendleft("Gi")

print(ticket_queue)

ticket_queue.pop()

print(ticket_queue)

#############


recent_files = deque(["core.py", "README.md", "__init__.py"], maxlen=3)

recent_files.appendleft("database.py")

print(recent_files)


#########

numbers = deque([1, 2])

numbers.extend([3, 4, 5])

numbers.extendleft([-1, -2, -3, -4, -5])

print(numbers)

