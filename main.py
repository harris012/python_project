import requests
import json

region = 193
URL = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=GEN,BEZ,BL,cases7_bl_per_100k,cases7_bl,death7_bl,cases,deaths,cases_per_100k,cases_per_population,BL_ID,last_update,cases7_lk,death7_lk&outSR=4326&f=json'
result = requests.get(URL)

output = json.loads(result.text)
refined = output['features']
data = [{k: v for k, v in d.items() if k == 'attributes'} for d in refined]

print(data)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

