import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}


response = requests.get("https://opentdb.com/api.php")
response.raise_for_status()
data = response.json()
qustion_data = print(data["results"])