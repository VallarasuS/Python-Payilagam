# primary_colors = { "red", "blue", "green" }

# primary_colors.add("yellow")
# primary_colors.add("red")
# primary_colors.remove("red")
# primary_colors.remove("red")

# print(primary_colors)
# print(type(primary_colors))


week_end = {"sat", "sun"}
week_days = {"mon", "tue", "wed", "thu", "fri"}

# union
days = week_days | week_end
print(days)

cricket_players = {"john", "adam", "abraham", "dave"}
basket_ball_players = {"john", "adam", "rob", "richard"}

# intersection
both_game_players = cricket_players & basket_ball_players
print(both_game_players)

# difference
only_cricket = cricket_players - basket_ball_players
print(only_cricket)

# symmetric difference
non_common_player = cricket_players ^ basket_ball_players
print(non_common_player)

bookings = ["john", "adam", "abraham", "dave", "john", "adam", "rob", "richard"]

uniques = set(bookings)

# for entry in bookings:
#     uniques.add(entry)

print(uniques)
