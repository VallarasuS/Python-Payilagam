students = ["John", "Dave"]
print(students)

students[0] = "John Adam"

john = students[0]
dave = students[1]

print(dave)

for student in students:
    print(student)

count = len(students)
print(count)

print(type(students))


# String functions
# upper
# lower

# strip
# lstrip
# rstrip

# find
# format

# split
# join


# list operation
# imagine a queue

# Add
# __________
# append
# insert (position)
# extend

# Delete
# ___________
# pop (position)
# clear

# change order
# --------------
# reverse
# sort

numbers = [1, 2, 7, 3, 5]
print(numbers)


total = 0

for num in numbers:
    print(num)
    total = total + num

print(total)

words = ["john", "45","23","76","87","98"]
numbers = words[1:len(words):1]

total = 0

for num in numbers:
    i = int(num)
    total = total  + i

print(total)