# -----------------------------------------
#   lists
# -----------------------------------------
#  A list is a collection of data elements
#   ------------------------------------
#   | 10 | 12 | 31 | 24 | 54 | 21 | 32 |
#   ------------------------------------
# -----------------------------------------

# int, float, string, boolean -> primitive data types

# list -> list of numbers, list of floats, list of strings, etc... -> composite data types

list_char = list()

list_numbers = [0, 1, 2, 3, 4, 5]
print(list_numbers)

list_numbers.append(0)
print(list_numbers)

list_numbers.remove(0)
print(list_numbers)

for num in list_numbers:
    print(num)

print(dir(list))
