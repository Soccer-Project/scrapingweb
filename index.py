import requests
from bs4 import BeautifulSoup as bs
import csv

seasons = [2021, 2020, 2019]
playersURL = [
    'https://www.transfermarkt.com/vinicius-junior/leistungsdaten/spieler/371998/plus/1?saison=',
    'https://www.transfermarkt.com/lionel-messi/leistungsdaten/spieler/28003/plus/1?saison=',
    'https://www.transfermarkt.com/neymar/leistungsdaten/spieler/68290/plus/0?saison=',
    'https://www.transfermarkt.com/gabriel-barbosa/leistungsdaten/spieler/244275/plus/1?saison='
    ]

players = ['Vinicius Junior', 'Messi', 'Neymar', 'Gabriel Barbosa']

def createCSV(file):
    with open(file, 'a') as csv_file:
        fieldnames = ['tournament', 'games', 'goals', 'assists']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()

def writeCSV(file, tournament, games, goals, assists):
    with open(file, 'a') as csv_file:
        fieldnames = ['tournament', 'games', 'goals', 'assists']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'tournament': tournament, 'games': games, 'goals': goals, 'assists': assists})
        csv_file.close()

def seedCSV(items, file):
    for item in items:
        tournament = item.find('td', {'class': 'hauptlink no-border-links'}).text
        status = item.findAll('td', {'class': 'zentriert'})
        times = item.findAll('td', {'class': 'rechts'})

        # titles = ['Jogos ', 'Gols ', 'Assists ', 'Entrou ', 'Saiu ', 'Amarelo ', '2-Amarelo ', 'Vermelho ', 'PKs ']
        titles = ['Jogos ', 'Gols ', 'Assists ']
        time = ['GM ', 'Played ']

        games = status[0].text
        goals = status[1].text
        assists = status[2].text

        writeCSV(file, tournament, games, goals, assists)

for season in range(len(seasons)):
    for n in range(len(players)):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

        url = playersURL[n] + str(seasons[season])

        data = requests.get(url, headers=headers)

        content = bs(data.content, "html.parser")

        tr_odd = content.findAll("tr", { 'class': 'odd' })
        tr_even = content.findAll("tr", { 'class': 'even' })

        print(players[n] + str(seasons[season]))
        print(url)

        file = './csvFiles/' + players[n] + ' ' + str(seasons[season]) +'.csv'

        createCSV(file)
        seedCSV(tr_odd, file)
        seedCSV(tr_even, file)
