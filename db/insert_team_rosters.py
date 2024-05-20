from create_tables import teams, players, draft_salaries, roster, player_gamelog
from insert_rows import insert_row
from nba_api.stats.static import teams as nba_teams_api
from nba_api.stats.static import players as nba_players_api
from nba_api.stats.endpoints import commonteamroster
import pandas as pd

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app
app.app_context().push()

team_ids = []
nba_teams = nba_teams_api.get_teams()
for team in nba_teams:
    team_ids.append(team['id'])
    
for team_id in team_ids:
    nba_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=2023).get_dict()
    for player_info in nba_roster['resultSets'][0]['rowSet']:
            insert_row(
            roster,
                team_id = player_info[0],
                season = player_info[1],
                league_id = player_info[2],
                player_name = player_info[3],
                nickname = player_info[4],
                player_slug = player_info[5],
                jersey_num = player_info[6],
                position = player_info[7],
                height = player_info[8],
                weight = player_info[9],
                birth_date = player_info[10],
                age = player_info[11],
                experience = player_info[12],
                college_school = player_info[13],
                player_id = player_info[14],
                how_acquired = player_info[15])