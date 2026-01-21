age = int(input("Enter your age: "))
voter_id_input = input("Do you have voter id? ")

has_voter_id = voter_id_input == "yes"
can_vote = age >= 18 and has_voter_id

print("Can Vote ? ", can_vote)

# Truthy VAlue


age = 34
accompanied_by_adult = True


def is_parent_present():
    print("Hello")
    return accompanied_by_adult


# short circute
allow_entry = age >= 18 or is_parent_present()

deny_entry = not allow_entry


print("Allow Entry ", allow_entry)


# children with access to tab
# allow access to specific sites only
# white_list -> .edu, .wiki, .org

# deny access to certain sites
# black_listed -> social, drugs, violence
