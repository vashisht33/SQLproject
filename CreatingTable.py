import sqlite3 as lit
#Creating table
def main():
    try:
        db=lit.connect("DataBase.db")
        cur = db.cursor()
        tablequery = "create table users(ID INT,Name TEXT,Contact_no TEXT)"
        cur.execute(tablequery)
        print("Table created successfully")
    except:
        print("Unable to create table")
    finally:
        db.close()

if __name__ == "__main__":
    main()