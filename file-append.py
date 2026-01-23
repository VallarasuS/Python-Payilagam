# read - r
# write - w
# append - a


def append(line):
    file = open(r"C:\Users\Valla\Desktop\temp\quotes.txt", "a")
    file.write(line)
    file.flush()
    file.close()


line = "\r\n If you are going through hell, keep going - Winston Churchill"
# append(line)

# \r - return
# \n - new line

lines = [
    "If you build it, they will come.	Joe Jackson (character) \r\n",
    "If you want something done right, do it yourself. -Charles-Guillaume Étienne \r\n",
]


def append_lines(lines):
    file = open(r"C:\Users\Valla\Desktop\temp\quotes.txt", "a")
    file.writelines(lines)
    file.flush()
    file.close()


append_lines(lines)


# # inventories.csv
# pen, 100, 10, 0, 0
# pencil, 200, 5, 0, 0

# # sales.csv
# pen, 10
# pencil, 10
# pen, 5
# pencil, 5

# # buy.csv
# pen, 10
# pencil, 10
# pen, 5
# pencil, 5
