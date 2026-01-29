# zero based index
# almost all sequences has index based access
message = "learning python is fun"

# access individual elements by index
index = 4
char_at_pos = message[index]
print(char_at_pos)

# slicing
# sub string / slice of sequence
# start: stop: step
sub_string = message[9:16:1]
print(sub_string)

n = 1

while n < 11:
    print(n)
    n = n + 1
