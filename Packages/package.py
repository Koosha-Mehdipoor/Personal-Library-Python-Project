
book_list = []
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
        print("The command is wrong try another time.")
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
    books_to_remove = []
    print("we entered to the delete funtion")
    name = input("please enter the name fo the book that you want to remove from the list: ")
    for index in range(len(book_list)):
        for key in book_list[index]:
            if book_list[index][key] == name:
                # the reason here I have added a secondry list to remove it later becuase during the iteration if I remove an element it will cause index error.
                books_to_remove.append(book_list[index])
                print(f"The book {name} will be removed from the list")
                break
            else:
                print("The book does not exist in your list")
    for book in books_to_remove:
        book_list.remove(book)
    print("Updated book list: ", book_list)