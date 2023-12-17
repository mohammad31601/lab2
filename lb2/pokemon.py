import requests
from bs4 import BeautifulSoup as soup
import csv

source = requests.get('https://pokemondb.net/pokedex/all')

# convert s to beautiful soup object
webpage = soup(source.content, features="html.parser")

P_id = []
P_Name = []
P_Type = []
P_Total = []
P_HP = []
P_Atk = []
P_Def = []
P_SpAtk = []
P_SpDef = []
P_Speed = []

# Find the table with the data
table = webpage.find(id='pokedex')

# Loop through rows in the table
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 0:
        data = [col.text.strip() for col in columns]
        P_id.append(data[0])
        P_Name.append(data[1])
        P_Type.append(data[2])
        P_Total.append(data[3])
        P_HP.append(data[4])
        P_Atk.append(data[5])
        P_Def.append(data[6])
        P_SpAtk.append(data[7])
        P_SpDef.append(data[8])
        P_Speed.append(data[9])

filename = 'Pokemon_ko.csv'

with open(filename, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id_no', 'Name', 'Type','Total', 'HP', 'Attack', 'Defense', 'Sp,Attack', 'Sp,Defense', 'Speed'])

    for i in range(len(P_Name)):
        writer.writerow([P_id[i], P_Name[i], P_Type[i], P_Total[i], P_HP[i], P_Atk[i], P_Def[i], P_SpAtk[i], P_SpDef[i], P_Speed[i]])