from create_tables import player_gamelog
from insert_rows import insert_row
import pandas as pd
from create_tables import db, teams, players, draft_salaries, roster, player_gamelog
from sqlalchemy import text

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app
app.app_context().push()


def select_all(table):
    sql_statement = "SELECT * FROM {a}".format(a=table)
    results = db.engine.execute(text(sql_statement)).fetchall()
    return results

def select_all_where(table, column, condition):

    sql_statement = "SELECT * FROM {a} WHERE {b} = {c}".format(a=table, b=column, c=condition)
    results = db.engine.execute(text(sql_statement)).fetchall()
    return results

def select_all_where_in(table, column, params):
    
    in_statement = "', '".join(map(str, params))
    in_statement = "('" + in_statement + "')"

    sql_statement = "SELECT * FROM {a} WHERE {b} IN {c}".format(a=table, b=column, c=in_statement)
    results = db.engine.execute(text(sql_statement)).fetchall()
    return results

def execute_raw_sql(sql_statement):
    results = db.engine.execute(text(sql_statement)).fetchall()
    return results