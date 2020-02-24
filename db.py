import sqlite3

def create_table():
    conn = sqlite3.connect('suzaku.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS binance_coins(Coin TEXT)')

create_table()
