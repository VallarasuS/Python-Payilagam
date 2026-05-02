# 5. Sum Square of even numbers up to 100

total = 0

for i in range(1, 101, 1):
    if i % 2 == 0:
        square = i ** 2
        total = total + square

print(total)