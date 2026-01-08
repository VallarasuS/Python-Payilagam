SIZE = 30


# String Util: justify words with space between them
def justify(prefix, suffix):
    left = str(prefix)
    right = str(suffix)
    return left.ljust(SIZE - len(right)) + right


# Pen & Pencil
# Track quantity, price and no of sold quantities of Pen & Pencil

# pen initial stock
pen_quantity = 100
pen_price = 20
pen_sold = 0

# pencil initial stock
pencil_quantity = 200
pencil_price = 10
pencil_sold = 0


def sell_pen(units):
    """
    Sells given units of pen to customers from the inventory.
    :param units: no of units to sell
    """
    global pen_quantity, pen_sold
    pen_quantity = pen_quantity - units
    pen_sold = pen_sold + units
    print("SELL: {0} unit of pen".format(units))


def buy_pen(units):
    """
    Buys given units of pen and added back to inventory

    :param units: Description
    """
    global pen_quantity, pen_sold
    pen_quantity = pen_quantity + units
    print("BUY: {0} unit of pen".format(units))


def status_pen():
    """
    Prints current inventories and sales
    """
    print(SIZE * "-")
    print("Pen".center(SIZE))
    print(SIZE * "-")

    print(justify("Quantity:", pen_quantity))
    print(justify("Price:", pen_price))
    print(justify("Sold:", pen_sold))

    print(SIZE * "-")
    print(justify("Revenue : ", pen_sold * pen_price))
    print(SIZE * "-")


status_pen()

sell_pen(2)
status_pen()

buy_pen(10)
status_pen()


def sell_pencil(units):
    """
    Sells given units of pencil to customers from the inventory.
    :param units: no of units to sell
    """
    global pencil_quantity, pencil_sold
    pencil_quantity = pencil_quantity - units
    pencil_sold = pencil_sold + units
    print("SELL: {0} unit of pen".format(units))


def buy_pencil(units):
    """
    Buys given units of pencil and added back to inventory

    :param units: Description
    """
    global pencil_quantity, pencil_sold
    pencil_quantity = pencil_quantity + units
    print("BUY: {0} unit of pen".format(units))


def status_pencil():
    """
    Prints current inventories and sales
    """
    print(SIZE * "-")
    print("Pencil".center(SIZE))
    print(SIZE * "-")

    print(justify("Quantity:", pencil_quantity))
    print(justify("Price:", pencil_price))
    print(justify("Sold:", pencil_sold))

    print(SIZE * "-")
    print(justify("Revenue : ", pencil_sold * pencil_price))
    print(SIZE * "-")


status_pencil()

sell_pencil(5)
status_pencil()

buy_pencil(20)
status_pencil()
