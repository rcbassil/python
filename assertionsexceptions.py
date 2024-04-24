#!/usr/bin/python3

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))

try:
    print (int(KelvinToFahrenheit(505.78)))
except Exception as e:
    print(e)
finally:
    print("Print with exception or not!")


try:
    print (KelvinToFahrenheit(-5))
except Exception as e:
    print(e)


def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])