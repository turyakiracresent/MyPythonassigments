# Initializing an empty dictionary
phone_book = {}

# Function to update the phone book
def add_contact(name, phone):
    phone_book[name] = phone

# Get user input for 3 names and phone numbers
for user in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    add_contact(name, phone)

# Print the entire phone book
print("\nPhone Book:")
for name, phone in phone_book.items():
    print(f"{name}: {phone}")

# Ask user to input a name and display the corresponding phone number
search_name = input("\nEnter a name to search for their phone number: ")
if search_name in phone_book:
    print(f"Phone number for {search_name}: {phone_book[search_name]}")
else:
    print(f"{search_name} not found in the phone book.")