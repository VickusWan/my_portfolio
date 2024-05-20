from create_tables import teams, players, draft_salaries, roster, player_gamelog, deadlines
from insert_rows import insert_row
from nba_api.stats.static import teams as nba_teams_api
from nba_api.stats.static import players as nba_players_api
import pandas as pd

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app
app.app_context().push()

# nba_teams = nba_teams_api.get_teams()
# for team in nba_teams:
#     insert_row(
#     teams,
#     id=team['id'],
#     full_name=team['full_name'],
#     abbreviation=team['abbreviation'],
#     nickname=team['nickname'],
#     city=team['city'],
#     state=team['state'],
#     year_founded=team['year_founded'])

# nba_players = nba_players_api.get_players()
# for player in nba_players:
#     insert_row(
#     players,
#     id=player['id'],
#     full_name=player['full_name'],
#     first_name=player['first_name'],
#     last_name=player['last_name'],
#     is_active=player['is_active']
#     )
    

df = pd.read_csv('draft_salary.csv')
for key, values in df.to_dict(orient='index').items():
    if values['POS'] == 'C' or values['POS'] == 'PF+C':
        temp = 'Center'
    elif values['POS'] == 'PG' or values['POS'] == 'SG' or values['POS'] == 'PG+SG' or values['POS'] == 'PG+SG+SF' or values['POS'] == 'PG+SG+PF':
        temp = 'Guard'
    else:
        temp = 'Forward'
    
    insert_row(draft_salaries,
    rank = values['Rank'],
    player_name = values['PLAYER'],
    five_position = values['POS'],
    three_position = temp,
    team = values['TEAM'],
    salary = values['TOTAL'])
    
# df = pd.read_excel('deadlines.xlsx')
# for key, values in df.to_dict(orient='index').items():
#     insert_row(deadlines,
#     gameweek = values['Gameweek'],
#     day = values['Day'],
#     deadline = values['Deadline'])