# Input
# Name, City, Math, Science, Language
# John, Chennai, 40, 60, 50
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

# Expected Output
# Name, City, Math, Science, Language, Total, Average, Top Score
# John, Chennai, 40, 60, 50, 150, 50, 60
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

# string
# - split \n
#   ignore first line
# - split by , -> 5 tokens or words
# process numerics, POS 2,3,4 []
# calculate sum, average, top
# add it back to the line
# using join / concatenation
# combine all lines

# Built-in fns:
# sum
# len
# max
# min
# type


def split_lines(source):
    lines = source.split("\n")
    return lines[1 : len(lines) : 1]


def split_tokens(source):
    words = source.split(",")
    return words[2 : len(words) : 1]


lines = split_lines(data)

for line in lines:
    tokens = split_tokens(line)
    print(tokens)

    total = 0
    top = 0

    for word in tokens:
        total = total + int(word)
        top = max(top, int(word))

    print(total)
    print(total / len(tokens))
    print(top)
