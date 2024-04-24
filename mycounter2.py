from collections import Counter


mynum=Counter([1,5,6,6,2,1])
print(mynum)

print(Counter(("abacate",3,4,"abacate",3,2)))

mynum.update({1:5})

print(mynum)

