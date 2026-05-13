# Write
# path
# mode - "w"

# Write
# IF file not exists, create new open
# If file exists overwrite

file = open(r"C:\Users\Valla\Desktop\data\marks.csv", "w")

line = "Vallarasu,50,60,70,80,90\n"
file.write(line)

lines = ["Sanjay,90,80,70,60,50\n"]
file.writelines(lines)

file.close()