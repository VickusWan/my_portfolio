import requests
import time
import os
import csv
from tqdm import tqdm

payload = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8,la;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": ""}

API = "RGAPI-a6182a1a-a6b0-462c-b89f-5d7e051405f3"
    
def fetch(typename, body):
    
    if body == 'AMERICAS':
        init = "https://americas.api.riotgames.com" 
        
    elif body == 'NA1':
        init = "https://na1.api.riotgames.com"
        
    else:
        return 'Not a proper URL'
    
    url = init + typename
    payload['X-Riot-Token'] = API
    re = requests.get(url,headers = payload)    
    if re.status_code == 404:
        return {}
    elif re.status_code == 200:
        time.sleep(1)
        return re.json()

def is_ARAM(matchId):
    typename = '/lol/match/v5/matches/{matchId}'.format(matchId = matchId)
    body = 'AMERICAS'
    data = fetch(typename, body)
    
    if not data:
        return False
    else:
        return data['info']['gameMode'] == 'ARAM'


start = 50000
end = 50550
bar = tqdm(total=(end-start), position = 0)
count = 0
with open('no_duplicates.csv', newline='') as csvfile, open('aram_games.csv', 'a', newline='') as aram_file:
    filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for _ in range(start - 1):
        next(filereader, None)
        count += 1
    
    for row in filereader:
        bar.update(1)
        print(is_ARAM(row[0]), row[0])
        if (is_ARAM(row[0])):
            
            csv_writer = csv.writer(aram_file)
            csv_writer.writerow(row)
