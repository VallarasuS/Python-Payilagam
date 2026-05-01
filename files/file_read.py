# # C:\Users\Valla\Desktop\temp\file_py.txt

# file = open(r"C:\Users\Valla\Desktop\temp\file_py.txt", "r")

# content = file.read()
# print(content)

# file.close()

# file = open(r"C:\Users\Valla\Desktop\temp\file_py.txt", "r")

# while True:
#     content = file.readline()
#     if content == "":
#         break
#     print(content)


# file.close()


file = open(r"C:\Users\Valla\Desktop\temp\file_py.txt", "r")
content = file.readlines()
print(content)
file.close()