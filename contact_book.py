def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Remove Contact")
    print("6. Exit")

def add_contact(contact_book):
    contact_name = input("Enter Contact Name: ")
    if contact_name in contact_book:
        print("Contact already exists with this name")
    else:
        contact_number = str(input("Enter Contact Number: "))
        contact_email = input("Enter the Email of the contact: ")
        contact_book[contact_name] = {"Number": contact_number, "Email": contact_email}
        print(f"Contact {contact_name} added successfully!")

def view_contact(contact_book):
    if not contact_book:
        print("No Contacts available")
    else:
        print("\n===== Contact Book =====")
        for n, (contact_name, contact) in enumerate(contact_book.items()):
            print(f"\nContact {n+1}:")
            print(f"Contact Name: {contact_name}")
            print(f"Contact Number: {contact['Number']}")
            print(f"Contact Email: {contact['Email']}")


def search_contact(contact_book):
    contact_name = input("Enter Contact Name to search: ")
    print("\n")
    if not contact_name in contact_book:
        print("No Contact Found!")
    else:
        print(f"Contact Name: {contact_name}")
        print(f"Contact Number: {contact_book[contact_name]['Number']}")
        print(f"Contact Email: {contact_book[contact_name]['Email']}")


def update_contact(contact_book):
    contact_name = input("Enter Contact Name to update: ")
    if not contact_name in contact_book:
        print("No Contact Found!")
    else:
        print("Enter the Parameter you want to update")
        print("1: Contact Number")
        print("2: Contact Email")
        update = int(input("Enter your choice: "))

        if update == 1:
            contact_number = str(input("Enter Contact Number: "))
            contact_book[contact_name]["Number"] = contact_number

        elif update == 2:
            contact_email = input("Enter the Email of the contact: ")
            contact_book[contact_name]["Email"] = contact_email

        else: 
            print("Invalid Choice!")

        print(f"Contact {contact_name} updated successfully!")
    

def remove_contact(contact_book):
    contact_name = input("Enter Contact Name to update: ")
    if contact_name in contact_book:
        del contact_book[contact_name]
        print(f"Contact {contact_name} removed successfully!")
    else:
        print("Contact not found")
    

def main():
    contact_book = {}  
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contact_book)

        elif choice == "2":
            view_contact(contact_book)

        elif choice == "3":
            search_contact(contact_book)

        elif choice == "4":
            update_contact(contact_book)

        elif choice == "5":
            remove_contact(contact_book)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
