def my_sort(line):
    flight_class = {'ECONOMY': 1,
                    'PREMIUMECONOMY': 2,
                    'BUSINESS': 3,
                    'FIRSTCLASS': 4}
    line_fields = line.strip().split() # split by space
    cabin_class = line_fields[-1] # last field
    return flight_class[cabin_class]
  
  
# reading flights.csv and storing in list
# variable contents
fp = open('Flights.txt')
contents = fp.readlines()

#print(contents)
  
# sorting based on categorical variable cabin class
contents.sort(key=my_sort)
  
# displaying contents on stdout after sorting
for line in contents:
    print(line)
  
fp.close()