# x = 1
# y = 2
# z = x + y

# print(z)


# def add(a, b):
#     return a + b


# z = add(5, 2)
# print(z)


# def incr(n):
#     return add(n, 1)


def add(a, b=1):
    return a + b


z = add(10)
print(z)

z = add(z)
print(z)

z = add(z)
print(z)

z = add(z, 3)
print(z)

scores = [50, 60, 70, 50]
marks = (50, 60, 70)

scores_tuple = tuple(scores)
marks_list = list(marks)
score_set = set(scores)


# inventory

# (quantity, price)
pen = (100, 10)


def purchase():
    pass


def sell():
    pass


def revenue():
    pass


def balance():
    pass
