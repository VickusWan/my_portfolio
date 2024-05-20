from create_tables import player_gamelog
from insert_rows import insert_row
from nba_api.stats.endpoints import playergamelog
import pandas as pd
import select_rows

import sys
import os
from app import app

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

app.app_context().push()

fantasy_team = ('Stephen Curry', 'Jamal Murray', 'Shai Gilgeous-Alexander', 'Austin Reaves', 'Demar Derozan', 'Jimmy Butler', 
 'Andrew Wiggins', 'Bennedict Mathurin','Victor Wembanyama', 'Nikola Jokic')

full_players = []
for player in select_rows.select_all('draft_salaries'):
    if "'" not in player[1]:
        full_players.append(player[1])
    

player_info = select_rows.select_all_where_in('players', 'full_name', tuple(full_players))

for player in player_info:
    gamelogs = playergamelog.PlayerGameLog(player_id=player[0], season='2023').get_dict()
    for game in gamelogs['resultSets'][0]['rowSet']:
            insert_row(
            player_gamelog,         
            season_id = game[0],
            player_id = game[1],
            game_id = game[2],
            game_date = game[3],
            matchup = game[4],
            win_loss = game[5],
            minutes = game[6],
            
            fgm = game[7],
            fga = game[8],
            fg_pct = game[9],
            
            fg3m = game[10],
            fg3a = game[11],
            fg3_pct = game[12],
            
            ftm = game[13],
            fta = game[14],
            ft_pct = game[15],
            
            oreb = game[16],
            dreb = game[17],
            reb = game[18],
            
            ast = game[19],
            stl = game[20],
            blk = game[21],
            tov = game[22],
            pf = game[23],
            
            pts = game[24],
            plus_minus = game[25],
            video_available = game[26])