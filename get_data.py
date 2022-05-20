import json
import os
import pandas as pd
import requests

from datetime import datetime
from pandas.io.json import json_normalize

# define variables
api_url = r'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
app_dir = os.path.abspath(os.path.dirname(__file__))
data_dir = app_dir + '/data/'

# download and normalize
d = json.loads(requests.get(api_url).text)
df = json_normalize(d, record_path=['features'])

# remove "attributes." from field names
colnames = []
for i in range(len(df.columns)):
    colnames.append(df.columns[i].replace('attributes.', ''))

df.columns = colnames

# extract last update date (for filename)
file_date = datetime.strptime(df['last_update'][0], '%d.%m.%Y, %H:%M Uhr').strftime("%Y%m%d_%H%M")

# epxort CSV to data directory, using last update date for filename
df.to_csv(
    path_or_buf = data_dir + "rki_" + file_date + ".csv",
    sep = ";",
    header = True,
    index = False,
    encoding = 'utf-8'
)
# create list of all exported CSV files
filepaths = [f for f in os.listdir((data_dir)) if f.startswith('rki_')]
filepaths

# append exported CSV files
rkitmp = []
for f in filepaths:
    dftmp = pd.read_csv(data_dir + f, sep = ";", decimal=",")
    rkitmp.append(dftmp)

# concat to Pandas data frame
rki = pd.concat(rkitmp, axis=0, ignore_index=True, sort = True)
rki = rki.drop_duplicates()

# export combined data
rki.to_csv(
    path_or_buf = data_dir + "rki.csv",
    sep = ";",
    header = True,
    index = False,
    encoding = 'utf-8'
)