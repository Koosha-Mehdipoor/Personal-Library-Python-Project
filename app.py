
import utils.SQLite_package as s


user_prompt = ("For adding a book to the list enter a:\n"
        "For reading info about a boook enter r:\n"
        "For deleting a book from the list enter d:\n"
        "For exiting from the program enter q:")

def menu():
    s.create_table()
    user_input = input(user_prompt)
    if user_input == "a":
        prompt_add_book()
    elif user_input == "r":
        prompt_read_book()
    elif user_input == "d":
        s.delete_book()
    elif user_input == "q":
        print("a presto!")
    else:
        print("The command is wrong try again.")
        menu()


def prompt_add_book():
    print("we entered to the add book function")
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    s.add_book(name,author,year)

def prompt_read_book():
    identifier = input("Please choose one the avialble options: name, author or all: ")
    if identifier == 'name':
        name = input("please enter the name of the book you are looking for: ")
        s.read_book(identifier,name)
    elif identifier == 'author':
        author = input("please enter the name of the author you are looking for: ")
        s.read_book(identifier,author)
    elif identifier == 'all':
        s.read_all_books("all","all")
    else:
        print("The command is wrong try again.")


menu()