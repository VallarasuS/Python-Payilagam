# Functions
# Group of statement to accomplish a task

# 1. Function with out parameter

# function definition
def print_five():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

# function call
print_five()

# 2. Function with parameters
def add(x, y):
    print("Total =", x + y)

# required parameters
add(10, 20)

# invalid, throws missing argument error
# add(10)
# add()

def divide(x , y):
    print (x / y)

# 3. Positional and Required Argument
divide(10, 2)
divide(2, 10)

# 4. Functions with return values
def multiply(x, y):
    return x * y

product = multiply(2, 3)
print(product)

# 5. Default Parameters

def multiply(x, y = 1):
    return x * y

product = multiply(2, 3)
print(product) # 6

product = multiply(2) # 2
print(product)

def add(x, y = 1):
    return x + y

total = add(2, 3) # 5
print(total)

total = add(2) # 3
print(total)

# 6. Variable Length Arguments
# *args - denotes variable length arguments

# throws error
# total = add(1, 2, 3)

def sum(*args): #args -> arguments - convention
    
    total = 0
    for n in args: # (1, 2, 3, 4, 5)
        total = total + n

    return total

total = sum(1, 2, 3, 4, 5)
print(total) # 15

total = sum(1, 2, 3, 4)
print(total) # 10

# required & positional arguments
def compute(x, y, add = True):

    if add:
        return x + y
    else: 
        return x - y

compute(10, 5)

# find total of parameters
# find product of parameters