from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from db.tables import db, poke, champinfo, aram_data
from db.select_testing_data import get_testing_data
import pandas as pd
from preprocessing import Preprocessing
import pickle

load_dotenv()
database_url = os.getenv("DATABASE_URL")
print("Database URL:", database_url)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/league')
def league():
    # champ_data = champinfo.query.with_entities(champinfo.champ_name, champinfo.image).all()
    # print(type(champ_data))
    # print(champ_data)

    df = pd.read_csv('champinfo.csv')
    champ_data = []
    
    for i in df[['champ_name', 'image']].iterrows():
        champ_data.append((i[1]['champ_name'], i[1]['image']))
    print(champ_data)
    return render_template('league.html', data=champ_data, value = '---', pics=None, champs=None)

@app.route('/nba')
def nba():
    return render_template('nba.html')

@app.route('/connectfour')
def connectfour():
    return render_template('connectfour.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    selected_value = request.form
    png_files = selected_value.getlist('dynamicDropdown')
    #summonerName = selected_value.getlist('summonername')
    
    # champ_data = champinfo.query.with_entities(champinfo.champ_name, champinfo.image).all()
    df = pd.read_csv('champinfo.csv')
    champ_data = []
    
    for i in df[['champ_name', 'image']].iterrows():
        champ_data.append((i[1]['champ_name'], i[1]['image']))
    final_values = [i.replace('.png', '') for i in png_files]
    
    for i in range(len(final_values)):
        if final_values[i] == 'Wukong' or final_values[i] == 'wukong':
            final_values[i] = 'MonkeyKing'
    
    col_names = ['champ_name_p', 'class_p', 'champ_difficulty_p', 'total_poke', 'hard_cc_champ']
    
    for i in range(len(final_values)):
        if i == 0:
            temp = get_testing_data(final_values[i], tuple([j+str(i+1) for j in col_names]))
        else:
            temp = pd.concat([temp, get_testing_data(final_values[i], tuple([j+str(i+1) for j in col_names]))], axis=1)
    
    pp = Preprocessing(temp)
    data = pp.fit()
    
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    win_pct = model.predict_proba(data)

    return render_template('league.html', data=champ_data, value = str(round(win_pct[0][1], 3)), pics=png_files, champs=final_values)

if __name__ == "__main__":
    app.run(debug=True)