import sqlite3 as lit

db = lit.connect("DataBase.db")
cur = db.cursor()

addcolumn = ("Alter table USERS1 add column Address varchar2")
cur.execute(addcolumn)
print("Column added successfully")