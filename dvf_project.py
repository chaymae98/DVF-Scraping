import pandas as pd
import requests
import json
import pypyodbc
import os

os.system("")

#df = pd.read_csv('full.csv')
df = pd.read_csv('full.csv', low_memory=False)
#df = pd.read_csv(filepath_or_buffer="full.csv" , sep=";", encoding_errors='ignore')
print(df.head())

'''lon = str(df['longitude'][1])
lat = str(df['latitude'][1])
url = "http://api.cquest.org/dvf?lat=" + lat+"&lon="+lon+"&dist=500"
print(url)

json_file = requests.get()
with open('output_file.json', 'wb') as f:
    f.write(json_file.content)
'''
r = requests.get('http://api.cquest.org/dvf?lat=48.85&lon=2.35&dist=200')
contenu = r.json()

print(contenu)


'''conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
'''
