import requests
import sys
apiKey = "081c7a4b3bbcea661c0799891be87f17"

city = input("What city or zip code would you like to check the weather for?\n")
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey+"&units=imperial"
request = requests.get(url)
json = request.json()

# print(json)

message = json.get("message")
if message:
    print("city not found -- exiting program")
    sys.exit
else:
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")



    print("Today's forecast in "+city+": "+description)
    print("   High: ",temp_max,"  ||  ","Low: ",temp_max)

# temperature = int(input("What is today's temperature? "))

# if temperature >= 80:
#     print("it's too hot... ")
#     print("let's just not go outside.")
# elif temperature <= 30:
#     print("it's kiiiiiinda cold.")
#     print("cuddle up inside today, mmkay?")
# else :
#     print("okay... you're allowed outside")

# print()
# print("press any key to continue")
# input()