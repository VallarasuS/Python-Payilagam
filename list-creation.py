#  LIST

# Collection of data
# It can contain multiple elements
# It can contain any type of data
# Can modify - mutable
# can contain duplicates

# CREATE

# - []
# - list(<seq>)

x = 1
y = 2
z = 3

# Creation

numbers = [1, 2, 3, 4]
person = ["Sam", 32, "B.Tech", 154.3, True]

print(person)

# Write
person[0] = "Adam"
print(person)

# Reading
age = person[1]
print(age)

# throws index out of range error
# age = person[10]
# print(age)

# numbers = [1, 2, 3, 4]
# for i in numbers:
#     print(i)

# start = 0
# stop = len(numbers)
# step = 1

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

numbers = [1, 2, 3, 4]
i = 0
while i < 4:
    value = numbers[i]
    numbers[i] = value * 2
    i = i + 1

print(numbers)

