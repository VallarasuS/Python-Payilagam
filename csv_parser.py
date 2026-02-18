from string_utils import split

# from task.csv import split_tokens

data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

lines = split(data, "\n", 1)

print(lines)

for line in lines:
    words = split(line, ",", 2)
    print(words)
