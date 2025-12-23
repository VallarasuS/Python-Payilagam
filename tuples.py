# nums = [1, 2, 3, 4, 5]


# def filter(source, predicate):
#     res = []
#     for i in source:
#         if predicate(i):
#             res.append(i)
#     return res


# even = filter(nums, lambda x: x % 2 == 0)
# print(even)


# def transform(source, converter):
#     res = []
#     for i in source:
#         output = converter(i)
#         res.append(output)
#     return res


# square = transform(nums, lambda x: x**2)
# print(square)


# # def reduce(num, aggregate):
# #     for i in nums:


# def length(source):
#     count = 0
#     for i in source:
#         count = count + 1

#     return count


# print(length(nums))
# print(len(nums))


# def add_function(x, y):
#     return x + y


# add_lambda = lambda x, y: x + y

# res = add_function(10, 20)
# print(res)

# res = add_lambda(20, 30)
# print(res)

# -List - []
# -Set - {"red", "blue", "green"}
# -Dictionary - {"key": "value"}

# -(1, ,2 3), ("John", 25, "IT")
# faster than tuple

# john = ["John", 23, "IT"]
# print(dir(john))

john = ("John", 25, "IT")
# print(dir(john))

name, age, department = john  # un-packing

print(name)
print(age)
print(department)


# scores.get("tamil")
# tamil + 10
# scores.set("tamil", res)


score = (60, 70, 80)
print(score)

tam, eng, math = score  # un-packing
tam = tam + 10

score = tam, eng, math  # packing
print(score)


def get_score(id):

    if id == 1:
        tam = 10
        eng = 20
        math = 30
        return tam, eng, math
    else:
        tam = 40
        eng = 50
        math = 60
        return tam, eng, math


student_one = get_score(1)
print(student_one)

tam, eng, math = get_score(2)
print(math)

tam = student_one[0]
eng = student_one[1]
math = student_one[2]
