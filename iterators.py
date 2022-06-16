#!/usr/bin/python3

cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

def iterable(obj):
     try:
         iter(obj)
         return True
     except TypeError:
         return False 
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, "iterable: ", iterable(element))


expertises = ["Python Beginner", 
              "Python Intermediate", 
              "Python Proficient", 
              "Python Advanced"]
expertises_iterator = iter(expertises)
print("Calling 'next' for the first time: ", next(expertises_iterator))
print("Calling 'next' for the second time: ", next(expertises_iterator))

other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break