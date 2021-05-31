import requests

astros = requests.get("http://api.open-notify.org/astros.json")
astros_response = astros.json()
iss_now = requests.get("http://api.open-notify.org/iss-now.json")
iss_now_response = iss_now.json()

print("People currently in space:")
for person in astros_response["people"]:
    print("  - ", person["name"])


print("---------")
print(iss_now_response)