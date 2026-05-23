total = 0

# i = 1
# while i <= 100:
#     total = total + i
#     i = i + 1

# print(total)

# data = "Hello from python"
# for i in data:
#     print(i)


# data = "Hello from python"

# i = 0
# while i < len(data):
#     x = data[i]
#     print(x)
#     i = i + 1


data = "Hello from python"
bucket = ""

for i in data:
    bucket = i + bucket

print(bucket)


data = "Hello from python"
bucket = ""

i = 0
while i < len(data):
    x = data[i]
    bucket = x + bucket
    i = i + 1

print(bucket)


data = "Hello from python"
count = 0
vowels = "aeiou"

for char in data:
    pass

    if char in vowels: # in - membership operator
        count = count + 1

    if vowels.find(char) > -1:
        count = count + 1

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count = count + 1

    a = 1
    b = 2
    z = 26

    A = 27
    B = 28
    Z = 52

    value = "N"

    # count lower case alphabet values

    if 1 <= value and value <= 26:
        count = count + 1

    


print(count)



password = "Password123#"

# for char in password:
#     # if char in "AZ":
#     # if char in "az":
#     # if char in "09":
#     # if char in "!@#$%^&*":
#     pass

# Extract only numbers from given string
# ex: "abc122dkjf834"
# Find total from csv data:
# ex: "John,45,23,76,87,98"