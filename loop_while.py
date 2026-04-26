# 1. Print  natural numbers up to given number,
# 5 -> 0, 1, 2, 3, 4

user_input = int(input("enter a number"))

# i = 0 # start
# while i < user_input: # stop
#     print(i)
#     i = i + 1 # step


# 2. Print natural numbers from given number to 1, 
# 5 -> 5, 4, 3,  2, 1

# i = user_input
# while i >= 1:
#     print(i)
#     i = i - 1

# 4.a Sum of numbers
# 1,2,3,4,5..... user_input

# i = 1
# sum = 0
# while i <= user_input:
#     sum = sum + i
#     i = i + 1

# print(sum)

# 4. Sum of even numbers

# i = 1 # start
# sum = 0

# while i <= user_input: # stop

#     if i % 2 == 0:
#         sum = sum + i

#     i =  i + 1 # step

# print(sum)

# 3. Find factorial of N

i = 1
factorial = 1

while i <= user_input:
    factorial = factorial * i
    i = i + 1

print(factorial)

# 5. SumSquare of even numbers
# 6. Sum of square of odd numbers
# 7. Given number check if it prime number
