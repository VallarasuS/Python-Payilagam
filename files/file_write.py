file = None

try:
    file = open(r"C:\Users\Valla\Desktop\temp\file_py.csv", "a")
    header = "name,quantity,price\n"
    file.write(header)
    data = "apple, 1, 400\n"
    file.write(data)
    data = "orange, 2, 350\n"
    file.write(data)

    contents = ["first line", "second line"]
    file.writelines(contents)
except Exception:
    print("Error, try again")
finally:
    file.close() 