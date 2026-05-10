from storage import load_contacts, save_contacts
from validators import get_valid_name, get_valid_phone, get_valid_email
from contacts import list_contacts, add_contact, search_contact, delete_contact
if __name__ == "__main__":

    contacts_details = load_contacts()

    while True:
        print("\n1. List all contacts")
        print("2. Add a contact")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_contacts(contacts_details)
        elif choice == "2":
            add_contact(contacts_details)
            save_contacts(contacts_details)

        elif choice == "3":
            search_name = input("Enter a name to search: ")
            found = search_contact(contacts_details,search_name)
            if found is None:
                print("Not found.")
            else:
                for key, value in found.items():
                    print(f"{key}: {value}")
        elif choice == "4":
            del_name = input("Enter a name to delete: ")
            deleted = delete_contact(contacts_details,del_name)
            if deleted:
                save_contacts(contacts_details)

        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")