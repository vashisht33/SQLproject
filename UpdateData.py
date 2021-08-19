import sqlite3 as lit

db=lit.connect("DataBase.db")

with db:
    newname ="AnkitaVashisht"
    user_id = 1
    cur = db.cursor()
    cur.execute("Update users set Name = ? where ID = ?",(newname,user_id))
    print("Data updated successfully")