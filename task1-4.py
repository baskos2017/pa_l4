import sqlite3
from datetime import datetime, timedelta

conn  = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

def create_table():
    query = """CREATE TABLE IF NOT EXISTS costs(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    assignment VARCHAR(255),
    cost FLOAT,
    profits FLOAT,
    time TEXT
    );"""

    cursor.execute(query)
    conn.commit()

create_table()


def add_info(assignment, cost, profits, time):
    query = f"""INSERT INTO costs (assignment, cost, profits, time)  VALUES ('{assignment}', '{cost}', '{profits}', '{time}');"""
    
    cursor.execute(query)
    conn.commit()

def costs_per_month():
    date = datetime.now()
    new_date = date - timedelta(days=30)
    query = f"""SELECT SUM(cost) FROM costs WHERE time BETWEEN '{new_date}' AND '{date}'"""
    cursor.execute(query)
    total_cost = cursor.fetchone()[0]
    print("Витрати за останні 30 днів:", total_cost)

def profit_per_month():
    date = datetime.now()
    new_date = date - timedelta(days=30)
    query = f"""SELECT SUM(profits) FROM costs WHERE time BETWEEN '{new_date}' 
    AND '{date}'"""
    cursor.execute(query)
    total_cost = cursor.fetchone()[0]
    print("Доходи за останні 30 днів:", total_cost)


while True:
    user_select = int(input('1 - Додати доходи, 2 - Додати витрати, 3 - Витрати за місяць, 4 - Доходи за місяцць, 0 - exit\n\n'))
    if user_select == 1:
        profits = int(input("profits: "))
        assignment = input("assignment: ")
        time = input("time: ")
        cost = 0 
        add_info(assignment, cost, profits, time)

    elif user_select == 2:
        profits = 0
        assignment = input("assignment: ")
        time = input("time: ")
        cost = int(input("cost: ") )
        add_info(assignment, cost, profits, time)
    elif user_select == 3:
        costs_per_month()
    elif user_select == 4:
        profit_per_month()
    elif user_select == 0:
        break