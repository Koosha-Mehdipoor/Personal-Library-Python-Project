text_menu = ("For adding a book to the list enter a:\n"
        "For reading info about a boook enter r:\n"
        "For deleting a book from the list enter d:\n")


def menu():
    user_input = input(text_menu)
    if user_input == "a":
        add_book()
    elif user_input == "r":
        read_book()
    elif user_input == "d":
        delete_book()
    else:
        print("The command is wrong try another time.")


    
def add_book():
    print("we entered to the add book function")

def read_book():
    print("we entered to the read book function")

def delete_book():
    print("we entered to the delete funtion")


menu()