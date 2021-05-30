# get the loan details
amount_owed = float(input("How much money is owed? (USD) \n")) # $50,000
apr = float(input("What is the APR of this loan? \n")) # 3%
payment = float(input("What is your monthly payment?\n")) # $1,000/month
months = int(input("How many months would you like to view?\n")) # 24 months


# get the monthly interest rate
monthly_interest = apr / 100 / 12

for i in range(months):
    # add in the interest
    interest_paid = amount_owed * monthly_interest
    amount_owed = amount_owed + interest_paid

    if (amount_owed > payment):
        # make a payment
        amount_owed = amount_owed - payment

        # print the results after this month
        print("Paid $", round(payment, 2), " this month, of which $", round(interest_paid, 2), " was interest.   ",sep='', end=' ')
        print("Now I owe $", round(amount_owed, 2), sep='')
    elif (amount_owed < payment and amount_owed > 0):
        months_hidden = months - i - 1
        print("FINAL PAYMENT! You paid off your loan of $", round(amount_owed, 2),  sep='')
        print("You paid off the loan in", i + 1, "months")
        break
