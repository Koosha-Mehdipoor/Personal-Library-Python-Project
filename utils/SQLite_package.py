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


def add_book():
    print("we entered to the add book function")
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    with DatabaseConnection('BOOKS.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO BOOKS VALUES (?,?,?)', (name,author,year))
    user_request()


def read_book():
    identifier = input(("Please choose one the avialble options: name, author or all: "))
    with DatabaseConnection('BOOKS.db') as connection:
        if identifier == 'name':

            name = input("please enter the name of the book you are looking for: ")
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM BOOKS WHERE name = ?;',(name,))
            print(cursor.fetchone())
            user_request()

        elif identifier == 'author':
            author = input("please enter the name of the author you are looking for: ")
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM BOOKS WHERE author =?;",(author,))
            print(cursor.fetchone())
            user_request()

        elif identifier == 'all':
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM BOOKS;")
            print(cursor.fetchall())
            user_request()
        else:
            print("The command is wrong try again.")
            menu()       


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