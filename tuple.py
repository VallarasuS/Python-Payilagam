# Non Primitive Data types
# list
# tuple
# set
# dict

# Primitive
# int
# str
# float
# bool

# List - []
# Tuple - ()

# Behavior
# Ordered collection of data
# Any data types
# Duplicates allowed
# Immutable data type (Can not modify)
    # faster
    # low memory usage

# Create

numbers = (1, 2, 3, 4)
numbers = tuple([1, 2, 3, 4])

for i in numbers:
    print(i)

x=  numbers[2]
print(x)

# error can not modify
# numbers[2] = 20

person = ("John", "John", 30,  "Chennai")
print(person)
print(type(person))

# un packing
name,lname, age, city = person
print(name)
print(age)
print(city)

packing
person = (name, age, city)
print(person)

print(person.index("John"))
print(person.count("John"))
