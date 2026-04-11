# age = input("enter your age")
# age = int(age)
# is_minor = age < 18
# print("Is Minor?", is_minor)

age = 18
is_major = age >= 18
print("Major ? ", is_major)

age = 20
has_vote_id = True
has_aadhaar = True
can_vote = age >= 18 and (has_vote_id or has_aadhaar)
print("Can Vote? ", can_vote)


math_score = 90
centum = math_score == 100
print("Centum?", centum)

go_signal = "green"
current_signal = "green"
should_i_stop = current_signal != go_signal

print("Stop?", should_i_stop)