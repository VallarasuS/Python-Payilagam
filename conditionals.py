# --------------------------------
#   if elif else
# --------------------------------
#
# if <expression>:
#   <block of code>
#
#
# --------------------------------
#
# if <expression>:
#   <block of code>
# elif <expression>:
#   <block of code>
#
#
# --------------------------------
#
# if <expression>:
#   <block of code>
# elif <expression>:
#   <block of code>
# else:
#   <block of code>
# --------------------------------


def evaluate(score):

    if score < 36:
        print("Failed")
    elif score == 100:
        print("Centum")
    elif score > 80:
        print("A Grade")
    elif score > 60:
        print("B Grade")
    else:
        print("C Grade")


score = input("enter math score: ")
evaluate(int(score))


def get_day(day):
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    else:
        return "Invalid Input"


day = input("enter day of week: ")
res = get_day(int(day))
print(res)
