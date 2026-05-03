# string - immutable data type
# mutation = change

# all operations will return a copy of the string

# upper
# lower

# split
# join

# strip
# lstrip
# rstrip

# find
# format

x = "Hello"
y = x.upper()
print(x)
print(y)

y = x.lower()
print(y)

x = "hello world"
y = x.title()
print(y)

x = "hello world"
y = x.split()
print(y)

z = "-".join(y)
print(z)

data_csv = "name,age,city"
print(data_csv)
tokens = data_csv.split(",")
data_pipe = "|".join(tokens)
print(data_pipe)

email = "-----john@gmail.com----"
# email = email.strip()
print(email)

email = email.lstrip("-")
print(email)

email = email.rstrip("-")
print(email)

# find if given char / string is found return pos
# if not found return -1

data = "Hello World"
x = data.find("world")
print(x)

data_template = "Rupees {0} deducted from your account {1} at location {2}"
text = data_template.format(1000, "ABC111", "Chennai")
print(text)

data = "XXXXaviour"
data = data[3:len(data):1]
print(data)