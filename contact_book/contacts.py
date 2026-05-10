from validators import get_valid_name, get_valid_phone, get_valid_email
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