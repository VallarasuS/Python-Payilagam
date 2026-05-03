name = "Sanjay Sugumar"
name = name.upper()

char_count = dict()

for c in name:
    count = char_count.get(c)

    if count == None:
        char_count.update({ c: 1 })
    else:
        char_count.update({ c: count + 1 })


print(char_count)