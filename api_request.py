import requests
import json

url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=4))