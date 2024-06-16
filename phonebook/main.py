# This program implements a simple phonebook application.
# It allows users to create, show, search, and delete contacts.

# Function to create a new contact and append it to the contacts.txt file.
def create_contact():
    with open("contacts.txt", 'a') as f:
        fname = input_fname()
        lname = input_lname()
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")

        name = fname + " " + lname
        f.write(f"[ {name} ,{phone_number}, {email} ]\n")
        print("Contact created successfully")

# Function to display all contacts from the contacts.txt file.
def show_contacts():
    with open("contacts.txt", 'r') as f:
        contacts = f.readlines()
        for contact in contacts:
            print(contact)

# Function to search for a contact by name in the contacts.txt file.
def search_contact():
    name = input("Enter the name to search: ")
    with open("contacts.txt", 'r') as f:
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
    with open("contacts.txt", 'r') as f:
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
            with open("contacts.txt", 'w') as f:
                f.writelines(contacts)  # Write the updated list back to the file
                print(f"{name} deleted from the phonebook.")
        else:
            print(f"{name} not found in the phonebook.")

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
        print("5. Exit")
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
            return 0  # Exit the program
            break
        else:
            print("Invalid choice")


# Run the main function if the script is executed directly.
if __name__ == "__main__":
    main()
