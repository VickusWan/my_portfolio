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

connection = psycopg2.connect(**db_params)

select_query = f'''
SELECT * from champinfo;
'''

df = pd.read_sql_query(select_query, connection)
connection.close()

df.to_csv("/mnt/c/Users/victo/OneDrive/Desktop/my_portfolio/champinfo.csv")