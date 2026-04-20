# key: Value

# - Key must be unique
# - Mutable data type
# - Can contain any type of data elements

employees = { "name": "John", "age": 35, "phone": 1236549870 }
print(type(employees))
print(employees)

# Read
name = employees["name"]
print(name)

age = employees["age"]
print(age)

# Write / Update
employees["age"] = 40
print(employees)