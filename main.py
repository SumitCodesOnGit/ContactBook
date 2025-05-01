import sqlite3
import contactBook

def menu():

    while True:
        print("--- contact book -------")
        print("1. Add contact")
        print("2. View Contacts")
        print("3. Update Contacts")
        print("4. Delete Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email id: ")
            contactBook.add_contact(name,phone,email)
        elif choice == '2':
            contactBook.view_contacts()
        elif choice == '3':
            contact_id = input("Enter the ID of the contact to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contactBook.update_contact(contact_id,name,phone,email)
        elif choice == '4':
            contact_id = input("Enter the id of the contact to delete: ")
            contactBook.delete_contact(contact_id)
        elif choice == '5':
            contactBook.close_connection()
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    menu()
