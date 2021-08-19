import sqlite3 as lit

db = lit.connect("DataBase.db")
cur = db.cursor()
selectquery =("Select * from users")
cur.execute(selectquery)

rows = cur.fetchall()
for data in rows:
    print(data)