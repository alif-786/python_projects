import mysql.connector
from difflib import get_close_matches

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    password="password",
    user="root",
    database="phonebook"
)

# Create a cursor object
cursor = mydb.cursor()

# Create the database and table if they don't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS phonebook")
cursor.execute("USE phonebook")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INT UNSIGNED AUTO_INCREMENT,
        name VARCHAR(250),
        number VARCHAR(250),
        email VARCHAR(250),
        PRIMARY KEY (id)
    )
""")

# Define a function to show the menu
def show_menu():
    print("\n" + "="*40)
    print(" Phonebook Menu ".center(40, "="))
    print("="*40 + "\n")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Show All Contacts")
    print("6. Exit")

# Define a function to add a contact
def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO contacts (name, number, email) VALUES (%s, %s, %s)", (name, number, email))
    mydb.commit()
    print("Contact added successfully!")

# Define a function to search for a contact
def search_contact():
    name = input("Enter name: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + name + '%',))
    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for result in results:
            print(f"Name: {result[1]}")
            print(f"Number: {result[2]}")
            print(f"Email: {result[3]}\n")
    else:
        print("No results found!")

# Define a function to delete a contact
def delete_contact():
    name = input("Enter name: ")
    cursor.execute("DELETE FROM contacts WHERE name = %s", (name,))
    mydb.commit()
    print("Contact deleted successfully!")

# Define a function to update a contact
def update_contact():
    name = input("Enter name: ")
    cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    result = cursor.fetchone()
    if result:
        print("\nCurrent Details:")
        print(f"Name: {result[1]}")
        print(f"Number: {result[2]}")
        print(f"Email: {result[3]}\n")
        u_name = input("Enter new name: ")
        u_number = input("Enter new number: ")
        u_email = input("Enter new email: ")
        cursor.execute("UPDATE contacts SET name = %s, number = %s, email = %s WHERE name = %s", (u_name, u_number, u_email, name))
        mydb.commit()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Define a function to show all contacts
def show_all_contacts():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    if results:
        print("\nAll Contacts:")
        for result in results:
            print(f"Name: {result[1]}")
            print(f"Number: {result[2]}")
            print(f"Email: {result[3]}\n")
    else:
        print("No contacts found!")

# Main function
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            show_all_contacts()
        elif choice == "6":
            print("Exiting phonebook...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()