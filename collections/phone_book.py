# Phone Book
# 1. Add name and number
# 2. Search by name, or number
# 3. Show all contacts
# 4. Delete Contact by number

# LIST, TUPLE, SET, DICTIONARY

# Dictionary
# Key, Value
# Number, all other details
# {
#     "9486456123": { "name": "John", "phone": "9486456123" },
#     "9486456456": { "name": "Rob", "phone": "9486456456" }
# }

phone_book = {} # dict()
print("--------Phone Book------")

def add_contact():
    name = input("Enter name ")
    phone = input("Enter phone number ")
    phone_book[phone] = { "name": name, "phone": phone }

def show_contacts():
    print(phone_book)

def delete_contact():
    phone = input("Enter phone number to delete ")
    del phone_book[phone]

def find():
    term = input("Enter number or name to find")
    for contact in phone_book.values():
        if contact["name"].find(term) > -1 or contact["phone"].find(term) > -1:
            print(contact)

while True:
    option = input("Choose an option: (add, delete, show, find, exit) ")
    option = option.lower().strip()

    if option == "add":
        add_contact()
    elif option == "show":
        show_contacts()
    elif option == "delete":
        delete_contact()
    elif option == "find":
        find()
    elif option == "exit":
        break
    else:
        print("Invalid option")

print("End of Program")