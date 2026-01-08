SIZE = 30


# String Util: justify words with space between them
def justify(prefix, suffix):
    left = str(prefix)
    right = str(suffix)
    return left.ljust(SIZE - len(right)) + right


pen = (100, 20, 0, "Pen")
pencil = (200, 10, 0, "Pencil")


def status(product):
    """
    Prints current inventories and sales
    """
    # tuple unpacking
    quantity, price, sold, name = product

    print(SIZE * "-")
    print(name.center(SIZE))
    print(SIZE * "-")

    print(justify("Quantity:", quantity))
    print(justify("Price:", price))
    print(justify("Sold:", sold))

    print(SIZE * "-")
    print(justify("Revenue : ", sold * price))
    print(SIZE * "-")


# String Util: justify words with space between them
def sell(product, units):
    quantity, price, sold, name = product  # un-packing tuple
    quantity = quantity - units
    sold = sold + units

    return (quantity, price, sold, name)  # packing tuple


def buy(product, units):
    """
    Buys given units of pen and added back to inventory

    :param units: Description
    """
    quantity, price, sold, name = product  # un-packing tuple
    quantity = quantity + units

    return (quantity, price, sold, name)  # packing tuple


status(pen)

pen = sell(pen, 10)
status(pen)

pen = buy(pen, 10)
status(pen)

status(pencil)
pencil = sell(pencil, 5)
status(pencil)

pencil = buy(pencil, 5)
status(pencil)
