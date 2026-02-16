file = open(r"C:\Users\Valla\Desktop\file\data.txt", "w")

data = [
    "11. Hello World\n",
    "12. Hello World\n",
    "13. Hello World\n",
]

file.writelines(data)

# file.write("1. Hello World\n")
# file.write("2. Hello World\n")
# file.write("3. Hello World\n")

file.close()


# file = open("", "r")

# while True:
#     line = file.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break
