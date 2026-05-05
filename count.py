name = "Sanjay Parithi"

counter = {}

for i in name:
    count = counter.get(i)
    if count == None:
        counter.update({ i: 1 })
    else:
        counter.update({ i: count + 1 })

print(counter)