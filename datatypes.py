
# print is a function, that writes given data to output device

age = 32;
PI = 3.14;
hello = "Hello there!";

print(hello)

name = input("enter your name: ")
print("Hello " + name + ". Nice to meet you.")

age = input("enter your age: ")
print("Your age is: " + age )

phone = input("enter your phone: ")
print("Your phone number is: " + phone)

education = input("enter your education: ")
print("Your education is: " + education)

# Function
# def FUNCTION_NAME:
#   EXPRESSION / STATEMENT

# def read_write():
#     age = input("enter your age: ")
#     print("Your age is: " + age)

# read_write()

def read_write(field):
    data = input("enter your " + field + ": ")
    print("Your " + field + " is: " + data)


read_write("name")
read_write("age")
read_write("phone")
read_write("education")