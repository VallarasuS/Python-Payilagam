# ADD
# - append
# - extend
# - insert

# Delete
# - pop
# - remove
# - clear

# Order
# - sort
# - reverse

numbers = [1, 2, 3, 4, 5]
last = numbers.pop()
print(last)
numbers.insert(0, last)
print(numbers)

# un-packing
[one, two, three] = [10, 20, 30]
# list, tuple, set

# tail - recursion

print(one, three)


# n * n-1 * 1 (n > 0)


# # recursion
# def fact(acc, n):

#     if n == 1:
#         return acc * n

#     next = n - 1
#     print(next)

#     return fact(n * next, next)


# out = fact(1, 5)
# print(out)
