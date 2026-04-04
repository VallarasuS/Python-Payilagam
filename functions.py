# Function

# Named group of instructions

# Syntax

# def <function-name>():
#     <function-body>


# function definition
def hello():
    print("Hello World")


# function call
# hello()
# hello()
# hello()

# print("Out side function")

# def add(x, y):
#     total = x + y
#     print(total)

# add(10, 20)

def add(x, y=1):
    total = x + y
    print(total)

incr = add

incr(10)

# def greet(name):
#     print("Hello", name)

# greet("John")

# def calculate(operation, x, y):
#     if operation == "add":
#         print(x + y)
#     elif operation == "mul":
#         print(x * y)


# calculate("add", 10, 20)
# calculate("mul", 10, 20)

# function definition
# function call
# function parameter
# function with default parameters
# function with return types


def incr(x):
    return x + 1

result = incr(10)
print(result)