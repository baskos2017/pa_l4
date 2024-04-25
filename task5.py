from requests import get
from datetime import datetime
from json import loads as jloads
import sqlite3

conn  = sqlite3.connect('db_currency.sqlite3')

cursor = conn.cursor()

currency_list = ['USD', 'EUR', 'GBP']


def create_table():
    query = """CREATE TABLE IF NOT EXISTS currency(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    currency_name VARCHAR(255),
    currency_value REAL,
    current_date DATETIME
    );"""

    cursor.execute(query)
    conn.commit()

create_table()



def timenow():
    timenow = datetime.today().strftime("%B %d %H:%M:%S")
    return timenow


def get_currency():
    req = get("https://api.monobank.ua/bank/currency").text
    if 'errorDescription' not in req:
        with open('currency.json', 'w') as f:
            f.write(req)
        print(f'{timenow()}: Done')
    else:
        print(f'{timenow()}: Error')

def all_currency():
    with open('currency.json', 'r') as f:
        cur = jloads(f.read())
        USD_course = cur[0]["rateBuy"]
        EUR_course = cur[1]["rateBuy"]
        GBP_course= cur[3]["rateCross"]
    return USD_course, EUR_course, GBP_course

def save_currency(USD_course, EUR_course, GBP_course):
    query = f"""INSERT INTO currency (currency_name, currency_value, current_date) VALUES (
    '{currency_list[0]}', '{USD_course}', '{timenow()}'),
    ('{currency_list[1]}', '{EUR_course}', '{timenow()}'),
    ('{currency_list[2]}', '{GBP_course}', '{timenow()}');"""
    cursor.execute(query)
    conn.commit()


get_currency()
USD_course, EUR_course, GBP_course = all_currency()
save_currency(USD_course, EUR_course, GBP_course)

   
