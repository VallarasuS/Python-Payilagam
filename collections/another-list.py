# LIST

# ADD
# - append
# - insert
# - extend

# DELETE
# - pop
# - remove
# - clear

# RE-ORDER
# - reverse
# - sort

numbers = [10, 2, 3, 4, 5]
print(numbers)

list_data = ["one", 65.3, True, "two", 1]
print(list_data)

slice = list_data[2:5:1]
print(slice)

# two = list_data[3]
# print(two)

# nested = [[1, 2, 3], ["one", "two", "three"], True, False, "hello"]
# print(nested)
# nums = nested[0]
# print(nums)

# data = [["John", "20", "03", "40"], ["Dave", "30", "20", "04"]]
# print(data)

numbers = [10, 2, 2, 2, 30, 4, 50]

# print(dir(numbers))

# ADD
# - append
# - insert
# - extend

# numbers.append(10)

# numbers.insert(0, 5)

# another_list = [2, 4, 6, 8]
# numbers.extend(another_list)
# x = numbers + another_list


# DELETE
# - pop
# - remove
# - clear

# Stack LIFO
# x = numbers.pop()
# y = numbers.pop()

# print(x, y)
# numbers.remove(1)
# numbers.clear()
print(numbers)


# RE-ORDER
# - reverse
# - sort

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

x = numbers.count(2)
print(x)
