message = "Hello World"
print("OG: ", message)

# upper
# lower
# startswith
# endswith
# split
# join
# strip, lstrip, rstrip
# find
# format

# string - immutable data type
# can NOT modify string
# any operation will result in a copy

up = message.upper()
print(up)

low = message.lower()
print(low)

st = message.startswith("He")
print("startswith", st)

en = message.endswith("World")
print("endswith", en)

words = "Learning python is fun"
tokens = words.split()  # split(",")
print(tokens)

tokens = ["Hello", "World", "From", "Python"]
words = ",".join(tokens)
print(words)

user_input = "   John   "
print(user_input)
print(user_input.strip())
# print(user_input.lstrip())
# print(user_input.rstrip())


words = "Learning python is fun"
pos = words.find("fun")
print(pos)

print("OG: ", message)

template = "Hello {0}, Greetings for the day! Your order for {1} is completed"
email = template.format("John", "Laptop")
print(email)

email = template.format("Dave", "Keyboard")
print(email)
