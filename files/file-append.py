file = open(r"C:\Users\Valla\Desktop\file\data.txt", "a")

file.writelines(["16. Hello World\n", "17. Hello World\n"])
file.flush()
file.writelines(["16. Hello World\n", "17. Hello World\n"])
file.flush()
file.writelines(["16. Hello World\n", "17. Hello World\n"])
file.flush()
file.writelines(["16. Hello World\n", "17. Hello World\n"])


file.close()
