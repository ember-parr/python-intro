import datetime
from datetime import date



# year = input('What year where you born?\n')
# month = input('Enter your numerical birth month (ex:January input: 1)\n')
# day = input('Enter your numerical birth date (ex: 4th input: 4)\n')
# print("you entered: " + str(month) + '/' + str(day) + '/' + str(year))
# input('Is this correct? (y/N) ')
# input()

# user_birthday = "2011-07-26"
user_birthday = input("input your birthday as YYYY-MM-DD\n")
year, month, day = map(int, user_birthday.split('-'))
user_birthday = date(year, month, day)
print()
formattedEntry = user_birthday.strftime("%A %d. %B %Y")
print("You were born: ", formattedEntry)
print()
print("------------")
print()



today = date.today()


# days old
daysOld = today - user_birthday
daysOld = daysOld.days
formatedDaysOld = f"{daysOld:,d}"
print("You are", formatedDaysOld, "Days Old!")

# weeks old
weeksOld = int(daysOld) // 7
weeks_days = int(daysOld) % 7
print("You are", weeksOld, "weeks &", weeks_days, "days old")

# months old
monthsOld = today.year - user_birthday.year
monthsOld = monthsOld * 12
print("You are", monthsOld, "months old")
