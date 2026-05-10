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
