#  Comparison Operator

# <,
# >,
# >=,
# <=
# ==
# !=

x = 10
y = 20

is_x_big = x > y  # -> True, -> False
print("X Big: ", is_x_big)

is_y_big = y > x  # 20 > 10 -> True
print("Y BIG?: ", is_y_big)

is_x_equal_to_y = x == y  # True / False -> Boolean
print("X == Y ?", is_x_equal_to_y)

signal = "ABC"
should_stop = signal == "abc"
print("Stop: ?", should_stop)

age = 16  # input("enter age: ")
age = int(age)
can_vote = age >= 18

print("Vote ?:", can_vote)

is_minor = age < 18
print("Minor ? ", is_minor)

signal = "red"
can_go = signal != "Red"
print("Can Drive? ", can_go)

# case sensitive
print("RED" == "RED")
