from flask_sqlalchemy import SQLAlchemy
import sys
import os

# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, parent_dir)
# from app import app

db = SQLAlchemy()

class teams(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    abbreviation = db.Column(db.String(4), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    year_founded = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<teams {self.name}>'

class players(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<players {self.name}>'

class draft_salaries(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255), nullable=False)
    five_position = db.Column(db.String(255), nullable=False)
    three_position = db.Column(db.String(255), nullable=False)
    team = db.Column(db.String(4), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<draft_salaries {self.name}>'
    
class roster(db.Model):
    team_id = db.Column(db.String(255), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    league_id = db.Column(db.String(255), nullable=False)
    player_name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255), nullable=True)
    player_slug = db.Column(db.String(255), nullable=True)
    jersey_num = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(255), nullable=True)
    height = db.Column(db.String(10), nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    birth_date = db.Column(db.String(255), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    experience = db.Column(db.String(255), nullable=True)
    college_school = db.Column(db.String(255), nullable=True)
    player_id = db.Column(db.String(255), primary_key=True)
    how_acquired = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<roster {self.name}>'

class player_gamelog(db.Model):
    
    season_id = db.Column(db.String(255), nullable=True)
    player_id = db.Column(db.String(255), primary_key=True)
    game_id = db.Column(db.String(255), primary_key=True)
    
    game_date = db.Column(db.String(255), nullable=True)
    matchup = db.Column(db.String(255), nullable=True)
    win_loss = db.Column(db.String(5), nullable=True)
    minutes = db.Column(db.Integer, nullable=True)
    
    fgm = db.Column(db.Integer, nullable=True)
    fga = db.Column(db.Integer, nullable=True)
    fg_pct = db.Column(db.Float, nullable=True)
    
    fg3m = db.Column(db.Integer, nullable=True)
    fg3a = db.Column(db.Integer, nullable=True)
    fg3_pct = db.Column(db.Float, nullable=True)
    
    ftm = db.Column(db.Integer, nullable=True)
    fta = db.Column(db.Integer, nullable=True)
    ft_pct = db.Column(db.Float, nullable=True)
    
    oreb = db.Column(db.Integer, nullable=True)
    dreb = db.Column(db.Integer, nullable=True)
    reb = db.Column(db.Integer, nullable=True)
    
    ast = db.Column(db.Integer, nullable=True)
    stl = db.Column(db.Integer, nullable=True)
    blk = db.Column(db.Integer, nullable=True)
    tov = db.Column(db.Integer, nullable=True)
    pf = db.Column(db.Integer, nullable=True)
    
    pts = db.Column(db.Integer, nullable=True)
    plus_minus = db.Column(db.Integer, nullable=True)
    video_available = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<player_gamelog {self.name}>'

class deadlines(db.Model):
    gameweek = db.Column(db.Integer, nullable=True)
    day = db.Column(db.Integer, nullable=True)
    deadline = db.Column(db.String(255), primary_key=True)
    
    def __repr__(self):
        return f'<deadlines {self.name}>'