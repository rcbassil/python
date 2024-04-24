from collections import Counter



print(Counter("mississippi"))

print(set("mississippi"))

print(Counter(set("mississippi")))


letters = Counter({"i": 4, "s": 4, "p": 2, "m": 1})

letters.update("missouri")

print(letters)


sales = Counter(apple=25, orange=15, banana=12)

monday_sales = Counter(apple=10, orange=8, banana=3)

sales.update(monday_sales)

print(sales)

print(sales["banana"])

for fruit in sales:
    print(fruit, sales[fruit])


for fruit, num in sales.items():
    print(fruit, num)


print(sales.keys())
print(sales.most_common())
print(sales.most_common(1)) # most common
print(sales.most_common(2)) # 2 most common
most_c = sales.most_common()
least_c = most_c[::-1] # least common
print(least_c)
print(sales.items())

most_c.reverse() # least common
print(most_c)


