# set 
# create
numbers = {32, }

# no duplicates

enrollment = ["John", "James", "Dave", "Rob", "John"]

without_duplicate = set(enrollment)
print(without_duplicate)

# dictionary
dictionary = { "age": 32 }


team_soccer = { "John", "Rob", "Dave" }
team_kabadi = { "John", "Jose", "Adam" }

# union operator
all_players = team_kabadi | team_soccer
print(all_players)

# intersection 
common_player = team_soccer & team_kabadi
print(common_player)

# difference
only_soccer = team_soccer - team_kabadi
print(only_soccer)

# symmetric difference
players_without_common = team_soccer ^ team_kabadi
print(players_without_common)

# Arithmetic operators
# + - * /
# numbers  

# operator additional work

# compilers 
# rule engine

