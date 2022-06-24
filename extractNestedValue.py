# Python3 code to demonstrate working of 
# Extract values of Particular Key in Nested Values
# Using list comprehension + values() + keys() 
  
# initializing dictionary
test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
             'is' : {"a" : 15, "b" : 19, "c" : 20}, 
             'best' :{"a" : 5, "b" : 10, "c" : 2}}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))

for k,v in test_dict.items():
    print(k,v)
  
# initializing key
temp = "c"
  
# using keys() and values() to extract values
res = [sub[temp] for sub in test_dict.values() if temp in sub.keys()]
  
# printing result 
print("The extracted values : " + str(res)) 