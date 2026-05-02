# sum of even numbers upto 100

# for i in range(1, 101, 1):
#     print(i)

# for i in range(1, 101, 1):
#     if i % 2 == 0:
#         print(i)

total = 0
for i in range(1, 100, 1):
    if i % 2 == 0:
        total = total + i

print(total)