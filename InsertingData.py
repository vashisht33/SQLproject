import sqlite3 as lit

myusers =(
    (1,"Ankita","abc"),
    (2,"kanvi","defi"),
    (3,"Seenam","ghi")
)

db=lit.connect("DataBase.db")
with db:
    cur = db.cursor()
    cur.executemany("INSERT INTO users VALUES(?,?,?)",myusers)
    print("Data inserted successfully")
