import sqlite3 as lit

db =lit.connect("DataBase.db")
with db:
    user_id = 1
    cur =db.cursor()
    cur.execute("Delete from users where ID = ?",(user_id,))
    db.commit()
    print("data deleted successfully")