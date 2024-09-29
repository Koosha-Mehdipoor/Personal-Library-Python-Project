import json
import sqlite3

def load_data():
    try:
        with open('books.json', 'r') as content:
            json.load(content)
    except FileNotFoundError:
        return[]

def create_table():
     connection = sqlite3.connect('/Users/koosha.mehdipoor@igenius.ai/Documents/Book_management.db')
     cursor = connection.cursor()

     cursor.execute("DROP TABLE IF EXISTS BOOKS")

     create_replace_table = """ CREATE TABLE BOOKS (
            Id VARCHAR(255) NOT NULL,
            NAME CHAR(25) NOT NULL,
            AUTHOR CHAR(25),
            YEAR INT
     ); """
    
     cursor.execute(create_replace_table)
     connection.commit()
     connection.close()
            

def write_data(dictionary):
    book_list = load_data
    try:
        with open('books.json', 'r') as content:
              book_list = json.load(content)
    except json.JSONDecodeError:
        book_list = []
    with open('books.json','w') as write_content:
            book_list.append(dictionary)
            json.dump(book_list, write_content)
            print(book_list)

def menu():
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




def add_book():
    print("we entered to the add book function")
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    book_dict = {
        "name" : name,
        "author" : author,
        "year" : year
    }
    write_data(book_dict)



def read_book():
    print("we entered to the read book function")
    book_list = load_data
    try:
        with open('books.json', 'r') as content:
              book_list = json.load(content)
    except json.JSONDecodeError:
        book_list = []
    name = input("please enter the name of the book you are looking for: ")
    for index in range(len(book_list)):
        for key in book_list[index]:
            if book_list[index][key] == name:
                 print(book_list[index])
                 return book_list[index]
    
            else:
                print("The book does not exist")
    


def delete_book():
    print("we entered to the delete funtion")
    book_list = load_data
    try:
        with open('books.json', 'r') as content:
              book_list = json.load(content)
              print(book_list)
    except json.JSONDecodeError:
        book_list = []
    books_to_remove = []
    print(f"first block load data from json {book_list}")

    name = input("please enter the name fo the book that you want to remove from the list: ")
    for index in range(len(book_list)):
        for key in book_list[index]:
            if book_list[index][key] == name:
                # the reason here I have added a secondry list to remove it later becuase during the iteration if I remove an element it will cause index error.
                books_to_remove.append(book_list[index])
                print(f"The book {books_to_remove} will be removed from the list")
    with open('books.json','w') as write_content:
            for book in books_to_remove:
                    book_list.remove(book)
                    json.dump(book_list,write_content)



def new_request():
    new_request = input("Do you have any other request? (y/n)")
    if new_request == "y":
        menu()
    else:
        print("Stato un piacere")