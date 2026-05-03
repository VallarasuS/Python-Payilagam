# 1. Gracefully handle error
# 2. Try recover from error
# 3. Meaningful error message to users

# Syntax
# try
# except
# finally

# try:
#     file = open(r"C:\Users\Valla\Desktop\temp\file_py.txt", "r")
#     content = file.write("Hello")
#     print(content)
#     file.close()
# except Exception:
#     print("Unable to write to file, check user permission, try again later")

try:
    number_one = int(input("Enter a number"))
    number_two = int(input("Enter another number"))
    print(number_one / number_two)
except ValueError:
    print("Only number values are accepted, try again with valid numbers input")
except ZeroDivisionError:
    print("Can not divide by zero, provide a non zero value")
except Exception:
    print("Unable to perform action, try again")
finally:
    print("Clean up and exit")
    numbers = None
    numbers = [1, 2, 3,]
    print(numbers)
    numbers = None