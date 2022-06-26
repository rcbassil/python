from collections import defaultdict
from collections import Counter

# counting

things = defaultdict(int)

things["dogs"] = things["dogs"] + 1
things["dogs"] = things["dogs"] + 1
things["dogs"] = things["dogs"] + 1

things["cats"] = things["cats"] + 1

print(things)


####### grouping !!!!!

# grouping by pet

pets = [
     ("dog", "Affenpinscher", "1982"),
     ("dog", "Terrier", "1967"),
     ("dog", "Boxer", "1844"),
     ("cat", "Abyssinian", "3419"),
     ("cat", "Birman", "1234"),
]

group_pets = defaultdict(list)

print(group_pets)

for pet, breed, regnum in pets:
    group_pets[pet].append({"breed": breed, "regnum": regnum})

print(group_pets)


dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(list)

for department, employee in dep:
    dep_dd[department].append(employee)


print(dep_dd)

dd = defaultdict(int)

for department, _ in dep:
    dd[department] += 1

print(dd)


# Removing duplicates

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(set)

for department, employee in dep:
    dep_dd[department].add(employee)

print(dep_dd)

for k,v in dep_dd.items():
    print(k, len(v))



#### Counting again, couting repeated letters


s = 'mississippi'

dd = defaultdict(int)

for letter in s:
    dd[letter] += 1

print(dd)


counter = Counter('mississippi')

print(counter)


### Acumulating

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')

