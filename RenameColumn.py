import sqlite3 as lit

db = lit.connect("DataBase.db")
cur = db.cursor()

renamecolumn = ("Alter table USERS1 rename column Address to Address1")
cur.execute(renamecolumn)
print("Column renamed successfuly")

#For dropping table
droptable = ("Drop table UERS1")
cur.execute(droptable)


