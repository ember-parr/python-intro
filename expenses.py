# expenses = [12.50, 30.16, 14.99]
# total = sum(expenses)

# sep='' tells python how to seperate each part of the print statement. (default adds a space, we dont want that here)
# print("you spent: $", total, " on lunch this week.", sep='')


expenseCount = input("how many expenses did you have this week? ")
expenses = []
for i in range(int(expenseCount)):
    print("Enter amount", i + 1, ": ")
    expenses.append(float(input()))

print("all expenses: ")
print(expenses)
print("you spent: $", sum(expenses), " this week.", sep='')