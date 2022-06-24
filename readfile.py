
from collections import Counter

# for large files


with open("./mydata.txt") as file:
    for line in file:
        print(line.rstrip())


# reading file

with open("./mydata.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)


mydict = {}

for i in content_list:
    myl = i.split(";")
    print(myl)
    film = myl[0]
    director = myl[1]
    year = myl[2]
    if year in mydict.keys(): 
        mydict[year] = mydict[year] + [{film, director}]
    else:
        mydict[year] = [{film, director}]

print(mydict)

for i in mydict:
    print(i,len(mydict[i]))


mylist = []

for i in content_list:
    myl = i.split(";")
    print(myl)
    mylist = mylist + myl

print(mylist)




c = Counter(mylist)

print(c)
