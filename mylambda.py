
add_one = lambda x: x+1

print(add_one(5))


full_name = lambda first, last: "My name is " + first + " " + last

print(full_name("Rodrigo", "Bassil"))

l = [1, 3, 8]

print(list(map(add_one, l)))