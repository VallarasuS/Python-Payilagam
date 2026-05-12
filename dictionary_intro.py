# Dictionary
# Value Store

# List []
# Tupe ()
# Set {}
# Dictionary { "key": "value" }

employee = { "emp1001" : "Parithi", "emp1002" : "Sanjay" }

# get
# update

details = employee.get("emp1001")
print(details)

details = employee["emp1001"]
print(details)

employee.update({"emp1001": "Elamparithi"})
print(employee)

employee["emp1001"] = "Elamparithi"
print(employee)

# delete
del employee["emp1001"]

phone_book = {}

phone_book = { "parithi": "9087654321" }

# Phone Book
# Add
# update
# Find 
# Delete