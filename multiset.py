from collections import Counter
import math


multiset = Counter({1, 1, 2, 3, 3, 3, 4, 4})

print(multiset)

print(multiset.keys())

############

prices = {"course": 97.99, "book": 54.99, "wallpaper": 4.99}
cart = Counter(course=1, book=3, wallpaper=2)

print(prices)
print(cart)

total = 0

for product, units in cart.items():
    price = prices[product]
    subtotal = units * price
    total = total + subtotal
    print(f"{product:9}: ${price:7.2f} × {units} = ${subtotal:7.2f}")

print(total)

##############


inventory = Counter(dogs=23, cats=14, pythons=7)

adopted = Counter(dogs=2, cats=5, pythons=1)

inventory.subtract(adopted)

print(inventory)

new_pets = Counter({"dogs": 4, "cats": 1})

inventory.update(new_pets)

print(inventory)


#######

prime_factors = Counter()

print(prime_factors)

# Prime factors of 1836

prime_factors.update({2: 2, 3: 3, 17: 1})

print(prime_factors)

product = 1

for factor in prime_factors.elements():
    product *= factor

print(product)


print(math.prod(prime_factors.elements()))