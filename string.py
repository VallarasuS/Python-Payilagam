# https://docs.python.org/3/library/stdtypes.html#textseq


# Truthiness Test
# "" -> False
# "Hello" -> True
# " " -> True

# format

first = "John"
last = "Abraham"
res = "Hello {0} {1}".format(first, last)
print(res)
# >> Hello John Abraham

template_string = "Hello {0}: Greetings, Your order value={1} is {2}."
email = template_string.format("John", 100, "confirmed")

template_string = "Hello {name}: Greetings, Your order value={value} is {status}."
email = template_string.format(name="John", status="confirmed", value=200)

# # lower, upper, title

message = "hello world"
lw = "Hello World".title()

user_name = input("Enter Your Name: ")
# strip, l, r
print(user_name.strip())  # "   John   Abraham  " -> "John    Abraham"
print(user_name.lstrip())  # "   John   Abraham   " -> "John   Abraham   "
print(user_name.rstrip())  # "   John   Abraham   " -> "   John   Abraham"

# split
# fruit, qty, price, variant
tokens = "apple,20,4,green".split(",")
print(tokens)

# startsWith, endswith
course_one = "be - CS"  # User Input
course_two = "BSC - CS"

if course_one.upper().startswith("BE"):
    print("Engineer")
else:
    print("Non Engineer")


if course_one.lower().endswith("cs"):
    print("CS Graduate")

if course_two.endswith("cs"):
    print("CS Graduate")

# find
data = "Returns a copy of the string"
res = data.find("copy")
print(res)

# count
data = "Returns a copy of the string"
res = data.count("n")
print(res)

# join
data = "orange     apple"
tokens = data.split()
out_one = " ".join(tokens)
out_two = ",".join(tokens)

print(out_one)
print(out_two)

# replace
data = "orange, aple"
res = data.replace("aple", "apple")
print(res)


# # iterate
message = "orange apple"
for c in message:
    print(c)

print(len("Hello World"))

print(dir(str))

# index, slice, sub string
