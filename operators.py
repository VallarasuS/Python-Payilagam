x = 10
y = 5

print("x ->", x)
print("y ->", y)

# Arithmetic Operators

# add
def add (a, b):
    return a + b

res = add(x,y)
print("sum :", res)

# sub
def sub(a, b):
    return a - b

res = sub(x, y)
print("sub :", res)

# mul
def mul(a, b):
    return a * b

res = mul(x,y);
print("mul :", res)

# true div
def div(a, b):
    return a / b

res = div(x, y)
print("div :", res)

# floor div
def floor_div(a, b):
    return a // b

res = floor_div(x , y)
print(res)

# pow
def pow(a , b):
    return a**b

res = pow(x,y)
print("pow :", res)

# Comparison Operators

#lt
def is_minor(age):
    return age < 18

res = is_minor(12)
print("Is Minor: ", res)

#gt
def can_drive(age):
    return age > 18

res = can_drive(21)
print("Can Drive", res)

#eq
def is_centum(mark):
    return mark == 100

res = is_centum(99);
print("Is Centum :", res)

#noteq
# status = shipped, in-transit, out for delivery, delivered
def is_in_progress(status):
    return status != "delivered"

res = is_in_progress("shipped")
print("Is in progress :", res)

#lteq
def is_cold(temp):
    return temp <= 24

res = is_cold(18)
print("Is cold :", res)

#gteq
def is_hot(temp):
    return temp >= 33

res = is_hot(45)
print("Is hot :", res)


# Logical Operators

# and

# or

# not
