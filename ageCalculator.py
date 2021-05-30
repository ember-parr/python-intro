import datetime

# year = input('What year where you born?\n')
# month = input('Enter your numerical birth month (ex:January input: 1)\n')
# day = input('Enter your numerical birth date (ex: 4th input: 4)\n')
# print("you entered: " + str(month) + '/' + str(day) + '/' + str(year))
# input('Is this correct? (y/N) ')
# input()

date = input("Enter date in YYYY-MM-DD format\n")
year, month, day = map(int, date.split('-'))
date = datetime.date(year, month, day)
print()
print("final date: ", date)
print("year: ", year)
print("month:", month)
print()
print("------------")
print()

today = date.today()
print("today: ", today)