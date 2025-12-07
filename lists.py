# -----------------------------------------
#   lists
# -----------------------------------------
#   A list is a collection of data elements
#   ------------------------------------
#   | 10 | 12 | 31 | 24 | 54 | 21 | 32 |
#   ------------------------------------
# -----------------------------------------

# int, float, string, boolean -> primitive data types
# list -> list of numbers, list of floats, list of strings, etc... -> Non-Primitive / Composite data types

# List properties
# Mutable, can add / remove / modify elements
# Retains order of elements
# Can contain duplicates

# attributes of list
# print(dir(list))
# print("")

# creation of list
char = list("Hello World")
nums = [10, 20, 30, 40, 50]

print("--- Read at index")

# Zero based index access to read or write values
print(nums[0])  # -> 10
print(nums[2])  # -> 30
print(nums[4])  # -> 50

print("--- Append")

# add an element at the end of the list
nums.append(60)  # -> [10, 20, 30, 40, 50, 60]
print(nums[5])  # -> 60

print("--- Copy")

nums.clear()  # -> [] removes all elements
nums = [10, 20, 30, 40, 50]

# creates a copy (shallow) of list
nums_clone = nums.copy()

# any changes to list wont affect each others
nums_clone[0] = 100  # -> [100, 20, 30, 40, 50]
nums.append(10)  # -> [10, 20, 30, 40, 50, 100]

print(nums_clone)
print(nums)

print("--- Count")

# count of an element in a list
ten_count = nums.count(10)
print(ten_count)

print("--- Extend")

nums = [10, 20, 30, 40, 50]
another = [100, 200, 300, 400, 500]

nums.extend(another)  # -> [10, 20, 30, 40, 50, 100, 200, 300, 400, 500]
print(nums)

print("--- Index")
i = nums.index(100)  # -> 5
print(i)

print("--- Insert")
nums.insert(5, 500)  # -> [10, 20, 30, 40, 50, 500, 100, 200, 300, 400, 500]
print(nums)

print("--- Pop")
# removes last element in list -> Last in first out
nums.remove(50)  # -> [10, 20, 30, 40, 500, 100, 200, 300, 400, 500]
print(nums)

print("--- Reverse")
# reverse the order of elements in the list
nums.reverse()  # -> [500, 400, 300, 200, 100, 500, 40, 30, 20, 10]
print(nums)

print("--- Sort")
# Re-arrange elements in ascending order in-place
nums.sort()  # -> [10, 20, 30, 40, 100, 200, 300, 400, 500, 500]

for num in nums:
    print(num)
