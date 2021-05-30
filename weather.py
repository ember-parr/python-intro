temperature = int(input("What is today's temperature? "))

if temperature >= 80:
    print("it's too hot... ")
    print("let's just not go outside.")
elif temperature <= 30:
    print("it's kiiiiiinda cold.")
    print("cuddle up inside today, mmkay?")
else :
    print("okay... you're allowed outside")

print()
print("press any key to continue")
input()