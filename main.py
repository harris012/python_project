import requests
import json
result = requests.get("https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID=193%20&outFields=OBJECTID,%20GEN,%20BEZ,%20BL,%20cases,%20deaths,%20cases_per_population,%20cases7_per_100k,%20cases7_lk,%20death7_lk,%20cases7_bl_per_100k,%20cases7_bl,%20death7_bl,last_update&outSR=4326&f=json")

output = json.loads(result.text)
refined = output['features']
data = [{k: v for k, v in d.items() if k == 'attributes'} for d in refined]

print(data)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

