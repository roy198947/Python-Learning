import json
CONTACTS_FILE = "contacts.json"
def load_contacts():
    try:
        with open(CONTACTS_FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE,"w") as f:
        json.dump(contacts, f, indent=2)