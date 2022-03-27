import requests
import json
result = requests.get("https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=tTMygh7G3EqdEgi7KoKpvgdPUjHq2c2xp9bXqJiU&lat=40&lon=-105")

result.status_code

print(result.text)

print(result.json())