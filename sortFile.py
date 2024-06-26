### Sort File by Column

def my_sort(line):
    line_fields = line.strip().split(',')
    print(line_fields)
    amount = float(line_fields[2])
    return amount
  
  
# opening file MallSalesData.csv
# and getting contents into a list
fp = open('MallSalesData.csv')
contents = fp.readlines()

print(contents)
  
# sorting using our custom logic
contents.sort(key=my_sort, reverse=True)
  
# printing the sorting contents to stdout
for line in contents:
    print(line)
      
fp.close()