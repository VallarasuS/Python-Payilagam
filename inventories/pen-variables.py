SIZE = 30


def justify(prefix, suffix):
    """
    Justify words with space between them

    :param prefix: Description
    :param suffix: Description
    """
    left = str(prefix)
    right = str(suffix)
    return left.ljust(SIZE - len(right)) + right


# Pen
# Track quantity, price and no of sold quantities of Pen

# initial stock
quantity = 100
price = 20
sold = 0


# String Util: justify words with space between them
def sell(units):
    global quantity, sold
    quantity = quantity - units
    sold = sold + units


def buy(units):
    """
    Buys given units of pen and added back to inventory

    :param units: Description
    """
    global quantity, sold
    quantity = quantity + units


def status():
    """
    Prints current inventories and sales
    """
    print(SIZE * "-")
    print("Pen".center(SIZE))
    print(SIZE * "-")

    print(justify("Quantity:", quantity))
    print(justify("Price:", price))
    print(justify("Sold:", sold))

    print(SIZE * "-")
    print(justify("Revenue : ", sold * price))
    print(SIZE * "-")


status()

sell(2)
status()

buy(10)
status()
