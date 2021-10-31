import requests
from bs4 import BeautifulSoup as bs
import csv

seasons = [2021, 2020, 2019]
playersURL = [
    'https://www.transfermarkt.com/vinicius-junior/leistungsdaten/spieler/371998/plus/1?saison=',
    'https://www.transfermarkt.com/lionel-messi/leistungsdaten/spieler/28003/plus/1?saison=',
    'https://www.transfermarkt.com/neymar/leistungsdaten/spieler/68290/plus/0?saison='
    ]

players = ['Vinicius Junior', 'Messi', 'Neymar' ]

for n in range(len(players)):
    for season in range(len(seasons)):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

        url = playersURL[n] + str(seasons[season])
        # url = 'https://int.soccerway.com/players/vinicius-jose-paixao-de-oliveira-junior/474972/'

        # print(n)
        # print(url)

        data = requests.get(url, headers=headers)

        content = bs(data.content, "html.parser")

        tr_odd = content.findAll("tr", { 'class': 'odd' })
        tr_even = content.findAll("tr", { 'class': 'even' })

        print(players[n] + str(seasons[season]))
        print(url)

        with open('./csvFiles/' + players[n] + ' ' + str(seasons[season]) +'.csv', 'a') as csv_file:
                    fieldnames = ['tournament', 'games', 'goals', 'assists']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    csv_file.close()

                    def printData(items):
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

                            print(tournament)
                            for i in range(len(titles)):
                                print(titles[i])
                                print(status[i].text)

                            with open('./csvFiles/' + players[n] + ' ' + str(seasons[season]) +'.csv', 'a') as csv_file:
                                fieldnames = ['tournament', 'games', 'goals', 'assists']
                                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                writer.writerow({'tournament': tournament, 'games': games, 'goals': goals, 'assists': assists})

                                csv_file.close()

        printData(tr_odd)
        printData(tr_even)
