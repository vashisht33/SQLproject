import sqlite3 as lit
#Creating a DataBase
def main():
    try:
        db = lit.connect("DataBase.db")
        print("Database created")
    except:
        print("Operation Failed")

if __name__ == "__main__":
    main()

#Creating a Table