import requests
import csv
import json
import os, os.path

DIR = './csvFiles'
files = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]


for file in files:
    with open('./csvFiles/'+file) as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['tournament', 'games', 'goals', 'assists'])

        csv_reader.__next__()

        games = 0
        goals = 0
        assists = 0

        for row in csv_reader:
            # print( row['games'] + ', ' + row['goals'] + ', ' + row['assists'] )
            if row['games'] != '-':
                games += int(row['games'])
            if row['goals'] != '-':
                goals += int(row['goals'])
            if row['assists'] != '-':
                assists += int(row['assists'])

        players = { 
            'Vinicius Junior' : '1c93d8cc-9890-4475-964f-e58beb84f7c0',
            'Neymar' : '59e11799-1710-4b19-a1d2-8e82a7c83d23',
            'Messi' : 'a38e3f47-a1ee-4a17-b32b-2d732debd6b8',
            'Gabriel Barbosa': '74db1bd9-5635-4c76-a7dd-0ea3e0480fb8'
        }

        seasons = {
            '2019' : '82740e35-4aef-4ed4-afa1-f972ae119bbd',
            '2020' : '83368a3c-8dd0-4b28-b424-0995eb4d7976',
            '2021' : 'f726c6be-f2c6-47c6-931c-8962afa04860'
        }

        payload = json.dumps({
            'player_id': players[file[:-9]],
            'season_id': seasons[file[-8: -4:]],
            'games': games,
            'goals': goals,
            'assists': assists
        })  

        result = requests.post('http://localhost:5000/season/data', data = payload, headers = {'Content-Type': 'application/json'})
        print(result.text)
    
    os.remove('./csvFiles/'+file)
