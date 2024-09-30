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


def load_data_database():
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM BOOKS;")
    book_list = [{'name': row[0], 'author': row[1], 'year': row[2]} for row in cursor.fetchall]
    connection.close()
    return book_list


def add_book():
    print("we entered to the add book function")
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    connection = sqlite3.connect('BOOKS.db',timeout=10.0)
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO BOOKS VALUES ("{name}","{author}",{year})')
    connection.commit()
    connection.close()


def read_book():
    identifier = input("If you want to search the database by book name enter name or for searching by author write author ")
    if identifier == 'name':

        name = input("please enter the name of the book you are looking for: ")
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM BOOKS WHERE name ='{name}';")
        book_list = [{'name': row[0], 'author': row[1], 'year': row[2]} for row in cursor.fetchall]
        connection.commit()
        connection.close()
        return book_list
    
    elif identifier == 'author':
        author = input("please enter the name of the author you are looking for: ")
        connection = sqlite3.connect('BOOKS.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FORM BOOKS WHERE author ={author};")
        book_list = [{'name': row[0], 'author': row[1], 'year': row[2]} for row in cursor.fetchall]
        connection.commit()
        connection.close()
        return book_list
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



def double_check_with_user():
    confirm = input("Are you sure you want to delete the item? (y/n)")
    if confirm == 'y':
        return True
    else:
        menu