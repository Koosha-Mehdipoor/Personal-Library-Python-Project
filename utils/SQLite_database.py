from .database_connection import DatabaseConnection

def create_table():
     with DatabaseConnection('BOOKS.db') as connection:
        cursor = connection.cursor()
        create_replace_table = """ CREATE TABLE IF NOT EXISTS BOOKS (
                NAME CHAR(25) NOT NULL ,
                AUTHOR CHAR(25),
                YEAR INT
        ); """
    
        cursor.execute(create_replace_table)


def add_book(name,author,year):

    with DatabaseConnection('BOOKS.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO BOOKS VALUES (?,?,?)', (name,author,year))



def read_book(identifier,condition):
    with DatabaseConnection('BOOKS.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM BOOKS WHERE {identifier} = ?;',(condition,))
            print(cursor.fetchone())


def read_all_books(identifier,condition):
    with DatabaseConnection('BOOKS.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM BOOKS WHERE ? = ?;',(identifier,condition,))
            print(cursor.fetchall())



def delete_book(name,author):
    with DatabaseConnection('BOOKS.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM BOOKS WHERE name = ? AND author = ?;',(name,author,))
    print("The book is removed from database")
