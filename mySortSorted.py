
from collections import namedtuple
from datetime import datetime
from collections import ChainMap

# list
numbers = [6, 9, 3, 1]

num_sorted = sorted(numbers)

print(num_sorted)

print(numbers)

# tuple
numbers_tuple = (6, 9, 3, 1)

numbers_tuple_sorted = sorted(numbers_tuple)

print(numbers_tuple_sorted)

# set
numbers_set = {5, 5, 10, 1, 0}

numbers_set_sorted = sorted(numbers_set)

print(numbers_set_sorted)

# string

string_value = 'I like to sort'

sorted_string = sorted(string_value)

print(sorted_string)


sorted_string = sorted(string_value.split())
print(sorted_string)
print(' '.join(sorted_string))


words = ['banana', 'pie', 'Washington', 'book']

print(sorted(words, key=len))


names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case, key=str.lower))


##########


StudentFinal = namedtuple('StudentFinal', 'name grade')
bill = StudentFinal('Bill', 90)
patty = StudentFinal('Patty', 94)
bart = StudentFinal('Bart', 89)
students = [bill, patty, bart]

print(sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True))

#########

Runner = namedtuple('Runner', 'bibnumber duration')

runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
runners.append(Runner('2425234', 1490))
runners.append(Runner('1235234', 1620))

runners_by_duration = sorted(runners, key=lambda x: getattr(x, 'duration'))

print(runners_by_duration)
top_three_runners = runners_by_duration[:3]
print(top_three_runners)

##########

Expenses = namedtuple('Expenses','month expense')

myexpenses = []

myexpenses.append(Expenses('April', "${:,.2f}".format(1932.45)))
myexpenses.append(Expenses('May', "${:,.2f}".format(1988.93)))
myexpenses.append(Expenses('March',"${:,.2f}".format(1398.45)))
myexpenses.append(Expenses('January',"${:,.2f}".format(1298.49)))
myexpenses.append(Expenses('February',"${:,.2f}".format(1572.55)))
myexpenses.append(Expenses('June',"${:,.2f}".format(1654.32)))
myexpenses.append(Expenses('July',"${:,.2f}".format(1732.25)))

print(myexpenses)
print(myexpenses[0])
print(myexpenses[0].month)

for x,y in myexpenses:
    print(x, y)

final_myexdict = {}

def get_expense_dict(myexpenses):
    mydict = {}
    for i in myexpenses:
        myexdict = i._asdict()
        print(myexdict)
        mydict = ChainMap(mydict,myexdict)
    return mydict

final_myexdict = get_expense_dict(myexpenses)

print(final_myexdict.maps)


months = {"January":0, "February":1, "March":2, "April":3, "May":4, "June":5, "July":6, "August":7, "September":8, "October":9, "November":10, "December":11 }


def month_value(value):
    return months[value.month]

myexpenses_by_month = sorted(myexpenses, key=month_value)

# myexpenses_by_month = sorted(myexpenses, key=lambda day: datetime.strptime(day, "%d/%b/%Y"))

print(myexpenses_by_month)

#####

my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
print(my_dates)

######