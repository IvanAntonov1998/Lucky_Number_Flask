import requests
import json

session = requests.session()
data = {"guess": 0}
header = {"content-type":"application/json"}

r = session.get("http://127.0.0.1:1338/api/start_game")
if r.json() ["success"] == True:
    while True:
        data["guess"] = input("Guess the number > ")
        r = session.post("http://127.0.0.1:1338/api/guess_the_number", data=json.dumps(data), headers=header)

        json_data = r.json()
        print(json_data)
        if json_data["status"] == "You win":
            break

else:
    print("Loading error!")


