from .database_connection import DatabaseConnection
def menu():
    create_table()
    text_menu = ("For adding a book to the list enter a:\n"
        "For reading info about a boook enter r:\n"
        "For deleting a book from the list enter d:\n"
        "For exiting from the program enter q:")
    user_input = input(text_menu)
    if user_input == "a":
        add_book()
    elif user_input == "r":
        read_book()
    elif user_input == "d":
        delete_book()
    elif user_input == "q":
        print("a presto!")
    else:
        print("The command is wrong try again.")
        menu()


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
    user_request()


def read_book(identifier,condition):
    with DatabaseConnection('BOOKS.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM BOOKS WHERE {identifier} = ?;',(condition,))
            print(cursor.fetchone())
    user_request()

def read_all_books(identifier,condition):
    with DatabaseConnection('BOOKS.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM BOOKS WHERE ? = ?;',(identifier,condition,))
            print(cursor.fetchall())
    user_request()


def delete_book():
    name = input("Please enter the name of the book: ")
    author = input("Please enter the name of the author: ")
    with DatabaseConnection('BOOKS.db') as connection:
        if double_check_with_user() == True:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM BOOKS WHERE name = ? AND author = ?;',(name,author))
            print("The book is removed from database")
    user_request()



def double_check_with_user():
    confirm = input("Are you sure you want to delete the item? (y/n)")
    if confirm == 'y':
        return True
    else:
        menu()


def user_request():
    request = input("Do you have any other request? (y/n)")
    if (request == "y") or (request == "yes"):
        menu()
    elif (request == 'n') or (request == 'no'):
        print("a presto!")
    else:
        print("Command is wrong please choose from the existing options")
        user_request()

#menu()