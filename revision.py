message = "Hello World"  # string
print(message)

age = 18 + 1  # integer
print(age)

weight = 54.3  # float
print(weight)

voting_age = 18
can_vote = age >= voting_age  # comparison operator
print(can_vote)

name = input("Enter Your Name :")
print(name)

age_string = input("Enter your age: ")
age = int(age)
print(age)
print(type(age))

price = 20
quantity = 2

total = price * quantity
print("Total Price: ", total)

ticket = 200
popcorn = 150

head_count = 2

total = (ticket + popcorn) * head_count
print("Movie Expense : ", total)

my_expense = total / head_count
print("My Exp: ", my_expense)

print("True: ", 10 / 3)
print("Floor: ", 10 // 3)


# ----

age = 14
max_age_minor = 18
is_minor = age < max_age_minor

print("Is minor: ", is_minor)

score = 45
centum = 100

is_centum = score == centum
print("Score Centum? :", is_centum)

age = 14
has_voter_id = True

can_vote = (age > 18) and (has_voter_id == True)
print("Can Vote:", can_vote)

can_vote = not (age < 18) and (has_voter_id == True)
print("Can Vote:", can_vote)


score = 50
pass_score = 36

if score >= pass_score:
    print("PASS")
    print("Score: ", score)
else:
    print("FAIL")


if score == 100:
    print("PASS ", " Centum")
elif score < pass_score:
    print("FAIL")
else:
    print("PASS")


def function_name():
    print("Hello My  First Function")


function_name()


def add(x, y):
    print(x + y)


add(10, 20)


def add(x, y):
    return x + y


result = add(10, 20)
print(result)


# # ----------------------------

counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1

# print("--------------------")

for i in range(0, 5, 1):
    print(i)

# print("--------------------")

numbers = [10, 5, 2, 7, 8, 4, 23, 22, 6]
for i in numbers:
    print(i)

filtered_numbers = []

for i in numbers:
    print(i)
    if i % 2 == 0 and i >= 2 and i <= 8:
        filtered_numbers.append(i)

print(filtered_numbers)

for i in filtered_numbers:
    print(i**2)
