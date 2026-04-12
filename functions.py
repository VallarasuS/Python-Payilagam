# Functions
# Named group of instruction

# def <function_name> ():
#     <function_body>

# function_name()

# function definition
def print_one_to_ten():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)

# function call
# print_one_to_ten()
# print_one_to_ten()
# print_one_to_ten()

def archive_logs():
    pass
    # copy logs
    # paste logs remote disk
    # delete local logs
    # refresh market data cache


def greet():
    print("Hello")

greet()
greet()
greet()

def greet(name): # parameter
    print("Hello", name)

greet("John") # argument

def set_volume(level):
    print("Volume Set to", level)

set_volume(10)


def place_order(product, quantity):
    print("Order placed for ", product)
    return "Order Placed"

status = place_order("Book", 1)
print(status)
