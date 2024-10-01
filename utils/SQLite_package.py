import sqlite3

def menu():
    create_table
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


def add_book():
    print("we entered to the add book function")
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    connection = sqlite3.connect('BOOKS.db',timeout=10.0)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO BOOKS VALUES (?,?,?)', (name,author,year))
    connection.commit()
    connection.close()
    user_request()


def read_book():
    identifier = input(("Please choose one the avialble options: name, author or all: "))
    if identifier == 'name':

        name = input("please enter the name of the book you are looking for: ")
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM BOOKS WHERE name ='{name}';")
        connection.commit()
        print(cursor.fetchone())
        connection.close()
        user_request()
    
    elif identifier == 'author':
        author = input("please enter the name of the author you are looking for: ")
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM BOOKS WHERE author ='{author}';")
        connection.commit()
        print(cursor.fetchone())
        connection.close()
        user_request()

    elif identifier == 'all':
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM BOOKS;")
        connection.commit()
        print(cursor.fetchall())
        connection.close()
        user_request()
    else:
        print("The command is wrong try again.")
        menu()       


def delete_book():
    name = input("Please enter the name of the book: ")
    author = input("Please enter the name of the author: ")
    if double_check_with_user() == True:
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM BOOKS WHERE name = "{name}" AND author = "{author}";')
        connection.commit()
        print("Committed")
        connection.close()
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

