import sqlite3
import os

def Create_DB():
    # Code to create a new sqlite database if not exists
    if os.path.exists('api_list.db'):
        return("Database already exists.")
    else:
        # Create a new database file
        Connection = sqlite3.connect('api_list.db')
        Connection.close()
        return("Database created successfully.")

def DB_Connection():
    # Code to establish a connection to the sqlite database
    Connection = sqlite3.connect('api_list.db')
    pass

def DB_Create_Table():
    # Code to create a table in the sqlite database
    pass

def DB_Table_Drop():
    # Code to drop the table in the sqlite database
    pass

def DB_Insert_Data():
    # Code to insert data into the sqlite database
    pass