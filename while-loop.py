# --------------------------------
#   loop while
# --------------------------------
#
# while <expression>:
#   <block of code>
#
# --------------------------------

seconds = 1

while seconds <= 60:
    print(seconds)
    seconds = seconds + 1

# ----------------------

while True:
    print(seconds)
    seconds = seconds + 1

    if seconds > 60:
        break


# -----------------------------------------
# print given a number n, output n, n times
# -----------------------------------------
# | one | two | three |
# |-----|-----|-------|
# | 3   | 5   | 6     |
# | 3   | 5   | 6     |
# | 3   | 5   | 6     |
# |     | 5   | 6     |
# |     | 5   | 6     |
# |     |     | 6     |


number = 5

count = 1

while count <= number:
    print(number)
    count = count + 1
