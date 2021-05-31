import requests

astros = requests.get("http://api.open-notify.org/astros.json")
astros_response = astros.json()

print("There are currently", astros_response["number"], "people currently in space. They are:")
for person in astros_response["people"]:
    print("  - ", person["name"])


print("---------")