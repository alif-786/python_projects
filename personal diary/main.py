import uuid  # This imports the uuid module, which is used to generate unique identifiers.

# function for the main menu
def menu():
    print("1. write a diary entry")
    print("2. read a diary entry")
    print("3. update a diary entry")
    print("4. exit")

# function for the creating a diary entry 
def create_diary_entry():
    entry_id = str(uuid.uuid4())[:5]  # Generates a unique 5-character ID for the diary entry.
    with open("diary.txt", "a") as f:  # Opens the diary file in append mode.
        diary_content = input("Enter your diary entry: ")
        entry_format = f"[{entry_id}: {diary_content}]\n"
        f.write(entry_format)
        print("Entry added successfully")

def read_diary_entry():
    with open("diary.txt", "r") as f:  # Opens the diary file in read mode.
        entries = f.readlines()
        print("ENTRIES :- ")
        for entry in entries:
            print(f"Entry id : {entry[1:6]}")  # Prints the entry ID (characters 1-5).
            print(f"Entry : {entry[6:-2]}")  # Prints the entry content (characters 6 to second-last).
            print("-" * 25)

# function for updating the entry 
def update_entry():
    update_entry_id = input("Enter the entry id you want to update: ").lower().strip()
    with open("diary.txt", 'r') as f:
        entries = f.readlines()

    entry_found = False
    updated_entry = []
    for entry in entries:
        if entry[1:6] == update_entry_id:
            entry_found = True
            new_entry = input("Enter your new diary entry: ")
            entry_format = f"[{update_entry_id}: {new_entry}]\n"
            updated_entry.append(entry_format)
        else:
            updated_entry.append(entry)

    if entry_found:
        with open("diary.txt", 'w') as f:
            f.writelines(updated_entry)
        print("Entry updated successfully")
    else:
        print("Entry not found")


def diary():
    while True:
        print("\nWELCOME TO THE DIARY\n")
        menu()
        print("*" * 25)
        choice = int(input("Enter your choice: "))
        print("")
        if choice == 1:
            create_diary_entry()
        elif choice == 2:
            read_diary_entry()
        elif choice == 3:
            update_entry()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    diary()

