import requests

API_KEY = "07f0d55c0e71538594e3610a671fee98"

url = f"https://api.openweathermap.org/data/3.0/onecall?lat=-1.286&lon=36.817&appid={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)
