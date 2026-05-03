# add
# delete
# list
# exit

print("Phone Book")
print("----------")

print(" 1. add \n 2. delete \n 3. list \n 4. exit")

option = input("Choose an option: ")
option = option.lower()

storage = dict() # { "name": "1234567890" }

if option == "add":
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")

    storage.update({  name: phone })
    print(storage)


storage.update({ "john" : "123123123"   } )

del storage["john"]

print(storage)
