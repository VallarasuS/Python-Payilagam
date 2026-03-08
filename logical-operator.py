# - Arithmetic
# - Comparison
# - Logical

# AND OR NOT

# AND -> Both input must be True
# OR -> Any one must be True
# NOT -> Flip / Negate Input True -> False, False -> True

age = 16  # 16,18,17
has_voter_id = True  # False

# Short circuit: if one input fails stop further evaluation
can_vote = age >= 18 and has_voter_id
print("can_vote? ", can_vote)

# watching movie, 'U/A' must be an adult
# accompanied by Adult

age = 19
accompanied_by_adult = False

can_watch_movie = 19 >= 18 or accompanied_by_adult
print("Movie? ", can_watch_movie)

has_voter_id = True

print("Allow to Vote:", has_voter_id)
print("Deny vote", not has_voter_id)

#  child, teen, adults, seniors, vip
