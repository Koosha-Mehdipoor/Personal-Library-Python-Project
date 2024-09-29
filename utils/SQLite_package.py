import sqlite3


def create_table():
     connection = sqlite3.connect('BOOKS.db')
     cursor = connection.cursor()
     create_replace_table = """ CREATE TABLE IF NOT EXISTS BOOKS (
            NAME CHAR(25) NOT NULL ,
            AUTHOR CHAR(25),
            YEAR INT
     ); """
    
     cursor.execute(create_replace_table)
     connection.commit()
     connection.close()


def load_data_database():
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()

    load_data = "SELECT * FROM BOOKS;"
    
    cursor.execute(load_data)
    connection.commit()
    connection.close()