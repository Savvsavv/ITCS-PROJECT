def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone  # Store the contact in the dictionary
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts():
    if len(contacts) == 0:  # Check if contacts dictionary is empty
        print("No contacts available.")
    else:
        print("\n--- Contacts ---")
        for name in contacts:  # Loop through the dictionary
            print(f"Name: {name}, Phone: {contacts[name]}")

# Function to search for a contact
def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:  # Check if the contact exists
        print(f"Contact found - Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")

# Main program loop
while True:
    display_menu()  # Show the menu
    choice = input("Choose an option (1-4): ")

    # Check user input and call the appropriate function
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please choose a valid option.")

