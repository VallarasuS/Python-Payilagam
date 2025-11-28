# --------------------------------
#   loop for
# --------------------------------
#
# for <variable> in <seq>:
#    <block of code>
#
#
# --------------------------------
#   range(start, end, step)
#   start = start value (inclusive)
#   end = end value (exclusive)
#   step = increment start value by step value until end, exclusive of end
#
#   range(1, 10, 1) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
#   range(1, 11, 1) -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#   range(10, 1, -1) -> 10, 9, 8, 7, 6, 5, 4, 3, 2
#   range(10, 0, -1) -> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# --------------------------------

number = 5

for i in range(1, number + 1, 1):
    print(i)


# ----------------------

start = 10
end = 20

for a in range(10, end + 1, 1):
    print(a)
