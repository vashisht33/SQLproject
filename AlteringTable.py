import sqlite3 as lit

db = lit.connect("DataBase.db")
cur = db.cursor()
renametable = ("Alter table users rename to USERS1")
cur.execute(renametable)
print("Table name updated successfully")

