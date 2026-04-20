# List Operation

# Add
# - append
# - insert
# - extend

# Delete
# - pop
# - clear

# Re-arrange
# - sort asc / desc
# - reverse

numbers = [1, 2, 3, 4]
print(numbers)

numbers.append(5)
print(numbers)

numbers.insert(1, "Sam")
print(numbers)

numbers = [1, 2, 3, 4]
another_numbers = [5, 6, 7, 8]

numbers.extend(another_numbers)
print(numbers)

x = [9, 10, 11]

numbers.extend(x)
print(numbers)
