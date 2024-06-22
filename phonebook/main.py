# This program implements a simple phonebook application.
# It allows users to create, show, search, and delete contacts.

# Function to create a new contact and append it to the contacts.txt file.

import re  # Import the regular expression module

#function to check the number is valid or not 
def valid_phone_number():
    pattern = r'^[0-9]{10}$'
    phone_number = input("Enter the phone number: ")
    if re.match(pattern, phone_number):
        return phone_number
    else:
       print("Invalid phone number. Please try again.")
       valid_phone_number()

#function to check the email is valid or not 
def valid_email():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email = input("Enter the email:")
    if re.match(pattern,email):
        return email
    else:
        print("Invalid email address. Please try again.")
        valid_email()  # Recursively call the function until a valid email is entered


def create_contact():
    with open("phonebook/contacts.txt", 'a') as f:
        fname = input_fname()
        lname = input_lname()
        phone_number = valid_phone_number()
        email = valid_email()
        name = fname + " " + lname
        f.write(f"[ {name} ,{phone_number}, {email} ]\n")
        print("Contact created successfully")

# Function to display all contacts from the contacts.txt file.
def show_contacts():
    with open("phonebook/contacts.txt", 'r') as f:
        contacts = f.readlines()
        if contacts:  # Check if there are any contacts in the list
            for contact in contacts:
                each_conntact = contact.strip("[]").rsplit(",")# Split the contact into a list of parts
                name = each_conntact[0]
                phone_number = each_conntact[1]
                email = each_conntact[2].replace("]", "")# Remove any spaces from the email
                print(f"Name: {name}")
                print(f"Phone Number: {phone_number}")
                print(f"Email: {email}")
                print("-"*20)
        else:
            print("No contacts found")

# Function to search for a contact by name in the contacts.txt file.
def search_contact():
    name = input("Enter the name to search: ")
    with open("phonebook/contacts.txt", 'r') as f:
        contacts = f.readlines()
        for contact in contacts:
            if name in contact:
                print(contact)
                break
            else:
                print(f"{name} not found in the phonebook")

# Function to delete a contact by name from the contacts.txt file.
def delete_contact():
    name = input("Enter the name to delete: ")
    with open("phonebook/contacts.txt", 'r') as f:
        contacts = f.readlines()
        found = False
        for contact in contacts:
            if name in contact:
                contacts.remove(contact)  # Remove the contact from the list
                found = True
                break
            else:
                print(f"{name} not found in the phonebook")

        if found:
            with open("phonebook/contacts.txt", 'r+') as f:
                f.writelines(contacts)  # Write the updated list back to the file
                print(f"{name} deleted from the phonebook.")
        else:
            print(f"{name} not found in the phonebook.")

# function for updating the contact from the contact list
def update_contact():
    name = input("Enter the name to update: ").capitalize()
    with open("phonebook/contacts.txt", 'r+') as f:
        contacts = f.readlines()
        contact_found = False
        for i, line in enumerate(contacts):
            if name in line.split(', ')[0]:
                contact_found = True
                print("Enter the new details for the contact:")
                fname = input_fname()
                lname = input_lname()
                phone = valid_phone_number()
                email = valid_email()
                new_contact = format_contact(fname, lname, phone, email)
                contacts[i] = new_contact
                print("Contact updated successfully.")
                break
        if not contact_found:
            print(f"Contact with name '{name}' not found.")
        else:
            f.seek(0)
            f.truncate()
            f.writelines(contacts)

def format_contact(fname, lname, phone, email):
    return f"[ {fname} {lname}, {phone}, {email} ]\n"

# Function to get the first name from the user and format it correctly.
def input_fname():
    fname = input("Enter the name ")
    first_letter = fname[0].upper()
    rest = fname[1:].lower()
    return first_letter + rest

# Function to get the last name from the user and format it correctly.
def input_lname():
    lname = input("Enter the lastname ")
    first_letter = lname[0].upper()
    rest = lname[1:].lower()
    return first_letter + rest

# Main function to run the phonebook application.
def main():
    while True:
        print("\n WELCOME TO THE PHONEBOOK \n")
        print("1. Create Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. update Contact")
        print("5. Exit")
        print("-"*20)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_contact()
        elif choice == 2:
            show_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            update_contact()
        elif choice == 6:
            return 0 # Exit the program
            
        else:
            print("Invalid choice")


# Run the main function if the script is executed directly.
if __name__ == "__main__":
    main()
