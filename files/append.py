file = open(r"C:\Users\Valla\Desktop\data\marks.csv", "a")
data = ["John,10,20,30,40,50\n", "Dave,10,20,30,40,50\n"]
file.writelines(data)
file.close()