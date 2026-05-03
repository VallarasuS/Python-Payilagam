# Dictionary
    # { "key": "value" }

# Create
numbers = dict()
numbers = {"one": 1, "two": 2, "three": 3}

print(numbers)

#  read using key
x =  numbers["one"]
print(x)

# write using key
numbers["one"] = 100
print(numbers)

# LIST
# numbers = [1, 2, 3]
# x = numbers[2]

# prime use case
# get
# update

x = numbers.get("one")
print(x)

numbers.update({ "four": 4 })
print(numbers)

numbers.update({ "four": 40, "five": 5 })
print(numbers)


