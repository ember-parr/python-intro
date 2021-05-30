import datetime
from datetime import date

import locale
locale.setlocale(locale.LC_ALL, 'en_US')
numFormat = locale.format("%d", 1255000, grouping=True)
print("numFormat --> ", numFormat)

# year = input('What year where you born?\n')
# month = input('Enter your numerical birth month (ex:January input: 1)\n')
# day = input('Enter your numerical birth date (ex: 4th input: 4)\n')
# print("you entered: " + str(month) + '/' + str(day) + '/' + str(year))
# input('Is this correct? (y/N) ')
# input()

user_birthday = "2011-07-26"
# user_birthday = input("Enter birthday in YYYY-MM-DD format\n")
year, month, day = map(int, user_birthday.split('-'))
user_birthday = date(year, month, day)
print()
print("You entered: ", user_birthday)
print()
print("------------")
print()



today = date.today()

daysOld = today - user_birthday
daysOld = daysOld.days

# days old
formatedDaysOld = locale.format("%d", int(daysOld), grouping=True)
print("you are", formatedDaysOld, "Days Old!")

# weeks old
