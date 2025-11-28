# --------------------------------
#   Operators
# --------------------------------
# Arithmetic Operators
# Comparison Operators
# Logical Operators
# --------------------------------

x = 10
y = 5

print("x ->", x)
print("y ->", y)

# Arithmetic Operators


# add
def add(a, b):
    return a + b


res = add(x, y)
print("sum :", res)


# sub
def sub(a, b):
    return a - b


res = sub(x, y)
print("sub :", res)


# mul
def mul(a, b):
    return a * b


res = mul(x, y)
print("mul :", res)


# true div
def div(a, b):
    return a / b


res = div(x, y)
print("div :", res)


# floor div
def floor_div(a, b):
    return a // b


res = floor_div(x, y)
print(res)


# pow
def pow(a, b):
    return a**b


res = pow(x, y)
print("pow :", res)

# Comparison Operators


# lt
def is_minor(age):
    return age < 18


res = is_minor(12)
print("Is Minor: ", res)


# gt
def can_drive(age):
    return age > 18


res = can_drive(21)
print("Can Drive", res)


# eq
def is_centum(mark):
    return mark == 100


res = is_centum(99)
print("Is Centum :", res)


# noteq
# status = shipped, in-transit, out for delivery, delivered
def is_in_progress(status):
    return status != "delivered"


res = is_in_progress("shipped")
print("Is in progress :", res)


# lteq
def is_cold(temp):
    return temp <= 24


res = is_cold(18)
print("Is cold :", res)


# gteq
def is_hot(temp):
    return temp >= 30


res = is_hot(45)
print("Is hot :", res)

# Logical Operators

# and


def can_drive_legally(age, licensed):
    return age > 18 and licensed == True


res = can_drive_legally(16, False)
print("Can drive legally :", res)

# or


def can_go(signal):
    return signal == "green" or signal == "yellow"


# not
def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not is_even(num)


res = is_odd(17)
print("Is Odd :", res)


def is_warm(temp):
    return not is_cold(temp) and not is_hot(temp)


res = is_warm(28)
print("Is Warm :", res)
