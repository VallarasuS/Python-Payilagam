# Read      - r
# Write     - w
# Append    - a

# open (path, mode)
# r - raw string

# file = open(r"C:\Users\Valla\Desktop\marks.csv", "r")
# data = file.read()
# print(data)
# file.close()

# file = open(r"C:\Users\Valla\Desktop\marks.csv", "r")

# abc = file.readline()
# print(abc)

# xyz = file.readline()
# print(xyz)

# xyz = file.readline()
# print(type(xyz))
# print(len(xyz))

# file.close()


# file = open(r"C:\Users\Valla\Desktop\marks.csv", "r")

# while True:
    
#     line = file.readline()
#     print(line)

#     if(line == ""):
#         break

# file.close()

file = open(r"C:\Users\Valla\Desktop\marks.csv", "r")
data = file.readlines()
print(data)
file.close()