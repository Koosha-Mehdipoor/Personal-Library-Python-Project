text_menu = ("For adding a book to the list enter a:\n"
        "For reading info about a boook enter r:\n"
        "For deleting a book from the list enter d:\n")

book_list = []

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
    name = input("please enter the name of the book: ")
    author = input("please enter the name of the author: ")
    year = input("please enter the year of its publications: ")
    book_dict = {
        "name" : name,
        "author" : author,
        "year" : year
    }
    print(book_dict)
    book_list.append(book_dict)
    print(f"this is the print of list{book_list}")
    new_request = input("Do you have any other request? (y/n)")
    if new_request == "y":
        menu()
    else:
        print("Stato un piacere")


def read_book():
    print("we entered to the read book function")
    name = input("please enter the name of the book you are looking for: ")
    for index in range(len(book_list)):
        for key in book_list[index]:
            if book_list[index][key] == name:
                 print(book_list[index])
                 return book_list[index]
            else:
                print("The book does not exist")
                break



def delete_book():
    print("we entered to the delete funtion")
    name = input("please enter the name fo the book that you want to remove from the list: ")
    for index in range(len(book_list)):
        for key in book_list[index]:
            if book_list[index][key] == name:
                book_list.remove(book_list[index])
                print(f"The book {name} is removed from the list")
                print(book_list)
                break
            else:
                print("The book does not exist in your list")

menu()