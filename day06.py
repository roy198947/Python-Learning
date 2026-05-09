import json

CONTACTS_FILE = "contacts.json"

def load_contacts(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts, filename):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=2)

def get_valid_name():
    while True:
        name = input("Enter the name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_valid_phone():
    while True:
        phone = input("Enter number: ")
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("Phone must be exactly 10 digits.")

def get_valid_email():
    while True:
        email = input("Enter an email: ")
        if "@" in email:
            return email
        print("Email must have @.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for c in contacts:
        print(f"{c['name']}, {c['phone']}, {c['email']}")

def add_contact(contacts):
    user_name = get_valid_name()
    user_phone = get_valid_phone()
    user_email = get_valid_email()
    new_contact = {
        "name": user_name,
        "phone": user_phone,
        "email": user_email
    }
    contacts.append(new_contact)

def search_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None

def delete_contact(contacts,name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact Deleted")
            return True
    print("Contact not found")
    return False

contacts_details = load_contacts(CONTACTS_FILE)

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
        save_contacts(contacts_details, CONTACTS_FILE)

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
            save_contacts(contacts_details, CONTACTS_FILE)

    elif choice == "5":
        break
    else:
        print("Invalid option, try again.")
