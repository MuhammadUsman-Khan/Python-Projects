def show_menu():
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

def add_book(library):
    book_title = str(input("Enter the book title: "))
    if book_title in library:
        print("This book Already Exists!")

    else:
        author_name = str(input("Enter the Author's name: "))
        status = "Available"
        library[book_title] = {"Author": author_name, "Status": status}
        print(f"Book {book_title} Added successfully!")

def view_books(library):
    if not library:        
        print("No books Available!")
    
    else:
        print("\n===== Available Books =====")
        for book_name, book in library.items():
            n = 0
            print(f"{n+1}: {book_name} By {book['Author']} ({book['Status']})")

def search_book(library):
    book_title = str(input("Enter the Book Title to search: "))
    if not book_title in library:
        print("No Book Found of such title!")
    
    else:
        print("Book Found!")
        print(f"Title: {book_title}")
        print(f"Author: {library[book_title]['Author']}")
        print(f"Status: {library[book_title]['Status']}")

def remove_book(library):
    book_title = str(input("Enter the Book Title to delete: "))
    if not book_title in library:
        print("Book not Found!")
    
    else:
        del library[book_title]
        print("Book deleted successfully!")
        
def borrow_book(library):
    book_title = str(input("Enter the Book Title to borrow: "))
    if not book_title in library:
        print("Book not Found!")
    
    else:
        if library[book_title]["Status"] == "Available":
            print("Book borrowed successfully!")
            library[book_title]["Status"] = "Borrowed"
        
        else:
            print("Book is already borrowed!")

def return_book(library):
    book_title = str(input("Enter the Book Title to return: "))
    if not book_title in library:
        print("Book not Found!")
    
    else:
        if library[book_title]["Status"] == "Borrowed":
            print("Book retured successfully!")
            library[book_title]["Status"] = "Available"
        
        else:
            print("Book is already returned!")

        
    


def main():
    library = {}
    show_menu()
    while True:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            add_book(library)
        
        elif choice == 2:
            view_books(library)

        elif choice == 3:
            search_book(library)

        elif choice == 4:
            remove_book(library)

        elif choice == 5:
            borrow_book(library)

        elif choice == 6:
            return_book(library)

        elif choice == 7:
            print("Exiting the Library Management System. GoodBye!")
            break

        else:
            print("Invalid Choice! Please try Again.")

    
if __name__ == "__main__":
    main()