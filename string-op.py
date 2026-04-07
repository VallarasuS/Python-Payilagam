#  Collections

# Primitive Data types

# int
# float
# str
# bool

# Non Primitive Data types

# LIST - []
# Tuple - ()
# Set - {}
# Dictionaries - { key : values }


# String Operations

# - upper
# - lower
# - title

# - split
# - join

# - strip
# - lstrip
# - rstrip

# - find
# - format

message = "Hello World"

# upper, lower, title
#####################################

data_base_user = "usEr-oNe@gmail.com"
login_user =  "User-One@gmail.com"

db_user_upper = data_base_user.lower()
login_user_upper = login_user.lower()

print(db_user_upper, login_user_upper)

if db_user_upper == login_user_upper:
    print("Registered User")
else:
    print("Un-registered User")


# split, join
#####################################

hello = "hello from python"
print(hello.title())

data = "john,32,True,65"
tokens = data.split(',')
print(tokens)

new_data = "-".join(tokens)
print(new_data)

# strip, lstrip, rstrip
#####################################

email = "  john@gmail.com  "
email = email.strip()
print(email)


email = "__john@gmail.com___"
email = email.strip("_")
print(email)

email = "__john@gmail.com___"
email = email.lstrip("_")
print(email)


# find
#####################################

data = "hello from python"
pos = data.find("python") # 11
print(pos)

data = "hello from python"
pos = data.find("fun") # -1
print(pos)

# format
#####################################

template = "Hi {0}, your order {1} for {2} rupees"
output = template.format("John", "confirmed", 1000)
print(output)

status = "confirmed"
price = 1000
name = "john"

output = f"Hi {name}, your order {status} for {price} rupees"
print(output)


message = "Hello world"

for i in message:
    print(i)