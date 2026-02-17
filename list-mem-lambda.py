# ZeroDivisionError
# FileNotFoundError
# TypeError

# error = 1 / 0

# x = input("enter x")
# y = input("enter y")

# print(x / y)

# try:
#     file = open(r"C:\file\text.txt")
#     file.read()
# except FileNotFoundError:
#     print("File doesn't exist")
# finally:
#     file.close()


try:
    print("10" / "0")
except ZeroDivisionError:
    print("Error: Can not divide by zero")
except TypeError:
    print("Error: Invalid type")
except Exception:
    print("Something went wrong")

print("EOP")

numbers = [1, 2, 3, 4, 5]
if 5 in numbers:
    print("Found")

res = []
for i in numbers:
    res.append(i * 2)

# List Comprehension
res = [i * 2 for i in numbers]
print(res)


numbers = [1, 2, 3, 4, 5, 6]
res = []

# for i in numbers:
#     if i == 0:
#         res.append(i)

# print(res)

# for i in numbers:
#     if i % 2 != 0:
#         res.append(i)

# print(res)


def filter(source, predicate):

    res = []
    for i in source:
        if predicate(i):
            res.append(i)

    return res


def map(source, transform):
    res = []
    for i in source:
        res.append(transform(i))

    return res


double = map(numbers, lambda i: i * 2)
double = map(numbers, lambda i: i * 3)


evens = filter(numbers, lambda i: i % 2 == 0)
odds = filter(numbers, lambda i: i % 2 != 0)
div_3 = filter(numbers, lambda i: i % 3 == 0)

res = [i for i in numbers if i % 2 != 0]
print(res)


# def add(x, y):
#     return x + y


add = lambda x, y: x + y
res = add(10, 20)
print(res)


try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can not divide by zero")
finally:
    print("Done")

numbers = [1, 2, 3]
print(3 in numbers)
double = [i * 2 for i in numbers]
even = [i for i in numbers if i % 2 == 0]
add = lambda x, y: x + y
