numbers = (1, 2, 3)
print(numbers)
print(type(numbers))

x = numbers[0]
print(x)

for i in numbers:
    print(i)

print(("one", 2, "three"))

# unpacking, de-construction
a, b, c = ("one", 2, "three")
x, y, z = [1, 2, 3]
print(x, z)

y = 20

# packing
new_numbers = (x, y, z)
print(new_numbers)

# numbers[0] = 10
