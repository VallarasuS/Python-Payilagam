# start, stop, step

message = "Hello World"

# indexed access - zero based
print(message[1])

# slicing - start:stop:step
# stop > excluded from result
slice = message[0:5:1]
print(slice)

slice = message[0 : len(message) : 2]
print(slice)
