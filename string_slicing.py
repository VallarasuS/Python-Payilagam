head_line = "Hello World!"

# split and iterate on words
for word in head_line.split(" "):
    print(word)

# string is an iterable sequence
for char in head_line:
    print(char)

# length of string
print(len(head_line))

# index access
print(head_line[0])

# slicing position 0 to 5 (exclusive of end index)
print(head_line[0:5])  # Hello

print(head_line[6:11])  # World
