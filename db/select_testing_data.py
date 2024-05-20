from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse
import pandas as pd
import sys
import pickle
sys.path.append('db')

load_dotenv()
database_url = os.getenv("DATABASE_URL")

url_parts = urlparse(database_url)
db_params = {
    'user': url_parts.username,
    'password': url_parts.password,
    'host': url_parts.hostname,
    'port': url_parts.port,
    'database': url_parts.path[1:],  # Remove the leading '/'
}

# def get_testing_data_pandas(champion, col_names):
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     aram_data = pd.read_csv('../aram_only_data.csv')
#     champinfo = pd.read_csv('../champinfo.csv')
#     poke = pd.read_csv('../cbamp_pokes.csv')
    
#     merged_df = aram_data \
#         .merge(champinfo[['champ_key', 'class', 'difficulty']], left_on='champId_p1', right_on='champ_key', how='left') \
#         .merge(poke[['Champ', 'total', 'hard CC']], left_on='champId_p1', right_on='champ_name', how='left')
        
        
#     result_df = merged_df.loc[merged_df['champId_p1'] == champion, 
#                               ['champId_p1', 'class', 'difficulty', 'total', 'hard CC']]
#     return result_df

def get_testing_data(champion, col_names):
    connection = psycopg2.connect(**db_params)
    
    select_query = f'''
    SELECT
    ad.{col_names[0]} , info1.class AS {col_names[1]}, info1.difficulty AS {col_names[2]}, 
    poke1.total AS {col_names[3]}, poke1.hard_cc AS {col_names[4]}
    FROM aram_data as ad
    LEFT JOIN champinfo as info1 ON ad.champ_id_p1 = info1.champ_key
    LEFT JOIN poke as poke1 ON ad.champ_name_p1 = poke1.champ_name WHERE ad.champ_name_p1=%s LIMIT 1;
    '''

    df = pd.read_sql_query(select_query, connection, params=(champion,))
    connection.close()
    return df

#ad.champ_name_p1, info1.class AS class_p1, info1.difficulty as champ_difficulty_p1, poke1.total as total_poke1, poke1.hard_cc as hard_cc_champ1