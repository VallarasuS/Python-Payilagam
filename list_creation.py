# # # list

# # # non-primitive data type

# # # Create
# # # - list()
# # # - []

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

names = ["Sanjay", "Parithi"]
print(names)

ex = [1, "two", 3.4, False]
print(ex)

ex = [1, [2, 3], 4]
print(ex)

numbers = [1, 2, 3, 4, 5]

# # index access, zero based index
print(numbers[4])

for num in numbers:
    print(num)

for char in "Password":
    print(char)

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i * 2)

total = 0

for i in numbers:
    total = total + i

print(total)


numbers = [1, 2, 3, 4, 5]
fact = 1

for i in numbers:
    fact = fact * i

print(fact)

numbers = [1, 2, 3, 4]
print(numbers[2])

numbers[2] = 20
print(numbers)

# Create
chars = list("Hello")
print(chars)

for c in "Hello":
    print(c)

# list()
# []

# any type,
# duplicates
# index based read, write
# loop - for, while

numbers = [1, 2, 3, 4, 5]

x = 0
while x < len(numbers):
    print(numbers[x])
    numbers[x] = numbers[x] ** 2
    x = x + 1

print(numbers)

for i in numbers:
    print(i**2)
