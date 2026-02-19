class Calculator:  # definition

    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y


calc_one = Calculator()  # construction / initialization

total = calc_one.add(10, 20)
print(total)

product = calc_one.mul(2, 3)
print(product)


calc_two = Calculator()

print(calc_one == calc_two)

# print(type(Calculator))
# print(type(calc_one))
