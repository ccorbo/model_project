import requests
from bs4 import BeautifulSoup
from game import Game
from tblnflgame_dao import insert_rows

teams_url = "https://www.pro-football-reference.com/teams/"

nfl_teams = {}

page = requests.get(teams_url)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all('table')
    table = soup.find('table', id='teams_active')
    for row in table.find_all('tr')[2:]:
        if not row.get('class'):
            th = row.find('th')
            a = th.find('a')
            url_parts = a['href'].split('/')
            nfl_teams[url_parts[2]] = th.text

for key, team in nfl_teams.items():
    url = f"https://www.pro-football-reference.com/teams/{key}/2019.htm"
    games = []
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', id='games')
        
        for row in table.find_all('tr')[2:]:
            game = Game()
            #print(row)
            game.team_key = key
            game.team =  team
            th = row.find('th')
            #print(th.text)
            setattr(game, th['data-stat'], th.text)
            tds = row.find_all('td')
            for td in tds:
                setattr(game, td['data-stat'], td.text)
                #print(td.text)
            games.append(game)
        insert_rows(games)
    else:
        print("Failed to get valid response from page")