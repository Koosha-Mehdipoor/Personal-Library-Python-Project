
import utils.SQLite_database as s

user_prompt = (
    "\n"
    "For adding a book to the list enter a:\n"
               "\n"
        "For reading info about a boook enter r:\n"
                "\n"
        "For deleting a book from the list enter d:\n"
                "\n"
        "For exiting from the program enter q:")

def menu():
    s.create_table()
    user_input = input(user_prompt)
    if user_input == "a":
        prompt_add_book()
    elif user_input == "r":
        prompt_read_book()
    elif user_input == "d":
        prompt_delete_book()
    elif user_input == "q":
        print("a presto!")
    else:
        print("The command is wrong try again.")
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

def double_check_with_user():
    confirm = input("Are you sure you want to delete the item? (y/n)")
    if confirm == 'y':
        return True
    else:
        menu()

def prompt_add_book():
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    if s.read_book("name",name) == None:
        s.add_book(name,author,year)
    else:
        print(f"The book {name} already exists in database.")
    user_request()

def prompt_read_book():
    identifier = input("Please choose one the avialble options: name, author or all: ")
    if identifier == 'name':
        name = input("please enter the name of the book you are looking for: ")
        s.read_book(identifier,name)
        user_request()
    elif identifier == 'author':
        author = input("please enter the name of the author you are looking for: ")
        s.read_book(identifier,author)
        user_request()
    elif identifier == 'all':
        s.read_all_books("all","all")
        user_request()
    else:
        print("The command is wrong try again.")
        prompt_read_book()


def prompt_delete_book():
    name = input("Please enter the name of the book: ")
    author = input("Please enter the name of the author: ")
    confirm = input("Are you sure you want to delete the item? (y/n)")
    if confirm == 'y' or confirm == 'yes':
        s.delete_book(name,author)
        user_request()
    else:
        menu()
menu()