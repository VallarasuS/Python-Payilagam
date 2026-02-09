# # numbers = (1, 2, 3)
# # print(numbers)
# # print(type(numbers))

# # x = numbers[0]
# # print(x)

# # for i in numbers:
# #     print(i)

# # print(("one", 2, "three"))

# # # unpacking, de-construction
# # a, b, c = ("one", 2, "three")
# # x, y, z = [1, 2, 3]
# # print(x, z)

# # y = 20

# # # packing
# # new_numbers = (x, y, z)
# # print(new_numbers)

# # # numbers[0] = 10

# l_numbers = [1, 2, 3, 4, 5]
# t_numbers = (1, 2, 3, 4, 5)

# # Tuples
# #  -   Better in terms of memory
# #  - Performance
# # - immutable


# def create_employee():
#     return "John", "EID013", "IT", 98


# e_one = create_employee()
# print(e_one)

# # un-packing
# name, eid, depart, data = create_employee()
# print(name, data)

t_numbers = (1, 2, 3, 4, 5)

# slicing
print(t_numbers[2 : len(t_numbers) : 1])

# for i in t_numbers:
#     print(i)

# print(t_numbers[0])
# # print(t_numbers[10])

# print(max(t_numbers))
# print(sum(t_numbers))


# Built in functions
# max, sum, min, len, type, dict,

data = "John", "Chennai", 40, 60, 50
print(type(data))
