#!?usr/bin/python3

from pandas import read_excel
import sqlite3
import config

def importPhone(filepath, msg):
    conn = sqlite3.connect(config.DATABASE_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS numbers")
    cur.execute("DROP TABLE IF EXISTS msg")
    cur.execute("""CREATE TABLE IF NOT EXISTS numbers (
                id INTEGER PRIMARY KEY,
                number TEXT);""")
    cur.execute("""CREATE TABLE IF NOT EXISTS msg (
                id INTEGER PRIMARY KEY,
                message TEXT);""")
    
    conn.commit()

    df = read_excel(filepath, 0)
    for index, (data) in df.iterrows():
        query = f'INSERT INTO numbers VALUES ("{index+1}","{data.iloc[0]}")'
        cur.execute(query)
        conn.commit()
        
    msg_query = f'INSERT INTO msg VALUES ("1", "{msg}")'
    cur.execute(msg_query)

    conn.commit()
    conn.close()