# age  = 16
# can_vote = age >= 18
# has_voter_id = True
# has_aadhaar = True

# # if age >= 18 and (has_voter_id or has_aadhaar):
# #     print("User can vote")
# # else:
# #     print("User can NOT vote")

# # print("End of Program")

# # # Nested If condition
# # if age >= 18:
# #     if has_aadhaar or has_voter_id:
# #         print("User Can Vote")
# #     else:
# #         print("User can NOT vote")

# if age >= 18:
#     if has_aadhaar:
#         print("User Can Vote")
#     elif has_voter_id:
#         print("user can vote")
#     else:
#         print("User can NOT vote")

# signal = "Red"

# if signal == "Red":
#     print("Stop")
# elif signal == "Green":
#     print("Go")
# elif signal == "Yellow":
#     print("Wait")
# else:
#     print("Watch and proceed")

# salary = 500000

# if salary <= 500000:
#     tax = 0
# elif salary <= 800000:
#     tax = 5
# elif salary <= 1200000:
#     tax = 12

# take_home = salary - (salary * tax / 100)

# box_a = 10
# box_b = 20

# if box_a > box_b:
#     print("Max ", box_a)
# else:
#     print("Max ", box_b)

# if box_a < box_b:
#     print("Min ", box_a)
# else:
#     print("Min ", box_b)

def find_min(x, y):
    if x < y:
        return x
    else:
        return y

a = input("Enter a number ")
a = int(a)

b = input("Enter a number ")
b = int(b)

min = find_min(a, b)
print("Min ", min)