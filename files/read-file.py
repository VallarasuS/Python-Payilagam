# file = open(r"C:\Users\Valla\Desktop\files\readme.txt", "r")
# contents = file.read()
# file.close()

# print(contents)


# file = open(r"C:\Users\Valla\Desktop\files\readme.txt", "r")
# line = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# line4 = file.readline()  #  None

# file.close()


# print(line)
# print(line2)
# print(line3)
# print(line4)

# verify EOF
# file = open(r"C:\Users\Valla\Desktop\files\readme.txt", "r")

# line = file.readline()

# while line != "":
#     print(line)
#     line = file.readline()

# file.close()

# print("EOF")

file = open(r"C:\Users\Valla\Desktop\files\readme.txt", "r")
lines = file.readlines()
file.close()

print(lines)
