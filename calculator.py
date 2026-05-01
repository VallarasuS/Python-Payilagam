# calculator
# print all options
#   add
#   mul
#   div
#   sub
#   exit

# get options from user
# get numbers from user
# perform operation
# print results
# repeat

while True:

    print("Calculator")
    print("----------")
    print(" add \n mul \n div \n sub \n exit")
    option = input("Select an option form above: ")
    option = option.lower()

    if option == "exit":
        break

    num1 = int(input("Enter number one"))
    num2 = int(input("Enter number two"))
    result = None

    if option == "add":
        result = num1 + num2
        print(result)
    elif option == "mul":
        pass
    elif option == "div":
        pass
    elif option == "sub":
        pass
    else:
        print("Invalid Input, try again")
