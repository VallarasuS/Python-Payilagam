x = 10
y = 20

is_x_less = x < y  # -> 10 < 20 -> True
print(is_x_less)

# admin_password = "1234"
# user_password = input("Enter Password > 1234")

# is_valid = admin_password == user_password
# print("Is password valid ? :", is_valid)

temperature = 100

has_fever = temperature >= 100
print("Fever Detected ? ", has_fever)

age = 16
is_minor = age < 18
print("Minor ? ", is_minor)

sign = "Red"
go = "Green"

should_stop = sign != go  # Red != Green -> True
print("Stop ? ", should_stop)

door_closed = "Closed"
status = "Closed"

can_deliver = status != door_closed
print("Can Deliver ?", can_deliver)


def can_deliver(status):
    return status != "Closed"


deliver = can_deliver("Open")
print("deliver : ", deliver)
