tax = 0.06

def _subtotal(arr):
    subtotal = 0
    for i in arr: 
        subtotal = subtotal + i
    return(subtotal)
purchases = []
purchases = [48, 18.4, 9.32]
n = len(purchases)
subtotal = sum(purchases)

taxDue = subtotal * tax
totalDue = subtotal + taxDue

name = input("What is your first name?\n")

print('Hey, ' + name + '! Your subtotal is: ', subtotal)
print('-- Tax: ', round(taxDue, 2))
print('Total Due: $', round(totalDue, 2))

input()
