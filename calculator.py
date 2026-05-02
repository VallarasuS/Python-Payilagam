def get_user_option():
    print("WELCOME CALCULATOR")
    print("------------------")
    print(" add \n sub \n divi \n muli \n exit")
    option = input("enter your above option:")

    return option.lower()


def calculate(option, num1, num2):

    result = None

    if option == "add":
        result = num1 + num2
    elif option == "sub":
        result = num1 - num2
    elif option == "divi":
        result = num1 * num2
    elif option == "muli":
        result = num1 / num2

    return result


def run_calculator():

    while True:

        option = get_user_option()

        if option == "exit":
            break

        num1 = int(input("enter a number one:"))
        num2 = int(input("enter a number two:"))

        result = calculate(option, num1, num2)
        print(result)


run_calculator()